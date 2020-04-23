import numpy as np
import math
from function_handler import FunctionHandler
from msd import SteepestDescentMethod
from gss import GoldenSectionSearch
from gui import GUI


parser = FunctionHandler()
gui = GUI(parser)

# example function
func = "math.sin(x ** 2 + 3 * y ** 2) / (0.1 + math.sqrt(x ** 2 + y ** 2) ** 2) + (x ** 2 + 5 * y ** 2) * (math.exp(1 - math.sqrt(x ** 2 + y ** 2) ** 2) / 2)"
parser.parse_function(func)

# prepare arguments
xlist = np.linspace(-10.0, 10.0, 300)
ylist = np.linspace(-5.0, 5.0, 400)
X, Y = np.meshgrid(xlist, ylist)

# draw example plot
gui.set_plot_data(X, Y, 20)
gui.draw_plot()

# enter main loop of GUI
gui.root.mainloop()
