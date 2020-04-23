import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI:
    def __init__(self, parser):
        matplotlib.use('TkAgg')

        self.parser = parser
        self.figure = None

        # main window
        self.root = tk.Tk()
        self.root.title('Metody optymalizacji')

        # events for quitting app
        self.root.bind("<Escape>", lambda _: self.root.quit())
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)

        # create main frame
        self.parser_frame = tk.Frame(self.root)
        self.parser_frame.grid(row=1, column=1, padx=10)

        # create frame for plot canvas
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")

        tk.Label(self.parser_frame, text="Funkcja", font='Helvetica 15 bold').grid(row=0, column=0)
        tk.Label(self.parser_frame, text='f(x) = ').grid(row=1, column=0)
        self.box = tk.Entry(self.parser_frame, width=20)
        self.box.grid(column=1, row=1)
        tk.Button(self.parser_frame, text="Parsuj i rysuj", command=self.parse_and_plot).grid(row=2, column=0)

    def parse_and_plot(self):
        self.parser.parse_function(self.box.get())
        self.draw_plot()

    def set_plot_data(self, x1_list, x2_list, levels=20):
        self.x1_list, self.x2_list = x1_list, x2_list
        self.levels = levels

    def draw_plot(self):
        fig = plt.figure(dpi=140)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Wykres funkcji')

        values = []
        for a, b in zip(self.x1_list, self.x2_list):
            values.append([])
            for x, y in zip(a, b):
                z = self.parser.function((x, y))
                values[-1].append(z)

        cp = plt.contourf(self.x1_list, self.x2_list, values, levels=self.levels)
        # cp = plt.contour(x1_list, x2_list, values, colors='black', levels=levels, linewidths=0.1)
        plt.colorbar(cp)

        plt.tight_layout(0.3)

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.get_tk_widget().grid(row=0, column=0, rowspan=3)
        canvas.draw()
