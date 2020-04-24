from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QCheckBox, QStyleFactory, QTextEdit, QPushButton, QGroupBox, QVBoxLayout, QRadioButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from function_handler import FunctionHandler


class Plot3D(FigureCanvas):
    def __init__(self, fig):
        self.figure = fig
        FigureCanvas.__init__(self, self.figure)

        self.plot_type = 'contour'

    def set_data(self, data):
        self.x = data[0]
        self.y = data[1]
        self.z = data[2]

    def set_plot_type(self, plot_type):
        if plot_type is True:
            self.plot_type = 'contour'
        else:
            self.plot_type = 'contourf'

        self.update_canvas()

    def update_canvas(self):
        self.figure.clear()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Wykres funkcji f(x, y)')

        if self.plot_type == 'contourf':
            cp = plt.contourf(self.x, self.y, self.z, levels=30)
            plt.colorbar(cp)
        else:
            cp = plt.contour(self.x, self.y, self.z, colors='black', levels=30, linewidths=0.1)

        self.draw()


class FunctionOptimizer(QDialog):
    def __init__(self, parser=None, parent=None):
        super(FunctionOptimizer, self).__init__(parent)
        self.setWindowTitle("Metody optymalizacji")
        QApplication.setStyle(QStyleFactory.create('Fusion'))

        self.parser = parser

        self.create_parser_box()
        self.create_plot_box()

        main_layout = QGridLayout()
        fig = plt.figure(dpi=100)

        self.fig_canvas = Plot3D(fig)
        main_layout.addWidget(self.fig_canvas, 0, 0, 3, 1)
        main_layout.addWidget(self.parser_group_box, 0, 1)
        main_layout.addWidget(self.plot_group_box, 1, 1)
        self.setLayout(main_layout)

    def create_parser_box(self):
        self.parser_group_box = QGroupBox("Parser")

        self.text_edit = QTextEdit()

        button = QPushButton("Parsuj")
        button.clicked.connect(lambda: self.update_function())

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(button)

        self.parser_group_box.setLayout(layout)

    def create_plot_box(self):
        self.plot_group_box = QGroupBox("Wykres")

        checkbox1 = QRadioButton("&Type 1")
        checkbox2 = QRadioButton("&Type 2")
        checkbox1.setChecked(True)
        checkbox1.toggled.connect(lambda x: self.fig_canvas.set_plot_type(x))

        layout = QVBoxLayout()
        layout.addWidget(checkbox1)
        layout.addWidget(checkbox2)

        self.plot_group_box.setLayout(layout)

    def update_function(self, data=None):
        func_to_parse = self.text_edit.toPlainText()
        self.parser.parse_function(func_to_parse)

        if data is not None:
            self.parser.set_mesh_ranges(data[0], data[1])

        self.fig_canvas.set_data(self.parser.create_mesh())
        self.update_figure()

    def update_figure(self):
        self.fig_canvas.update_canvas()
