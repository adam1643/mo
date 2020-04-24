from function_handler import FunctionHandler
from msd import SteepestDescentMethod
from gss import GoldenSectionSearch
from pyqt_gui import FunctionOptimizer, QApplication


# example function
func = "sin(x ^ 2 + 3 * y ^ 2) / (0.1 + sqrt(x ^ 2 + y ** 2) ** 2) + (x ^ 2 + 5 * y ^ 2) * (exp(1 - sqrt(x ** 2 + y ** 2) ^ 2) / 2)"

parser = FunctionHandler()
parser.parse_function(func)
parser.set_mesh_ranges((-10.0, 10.0), (-5.0, 5.0))

if __name__ == '__main__':
    app = QApplication([])
    gui = FunctionOptimizer(parser=parser)

    gui.text_edit.setPlainText(func)
    gui.fig_canvas.set_data(parser.create_mesh())
    gui.update_figure()

    gui.show()
    app.exec_()
