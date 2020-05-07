import math
from gss import GoldenSectionSearch
from function_handler import FunctionHandler


class SteepestDescentMethod:
    def __init__(self, dir_minimizer, f_handler=None):
        self.f_handler = f_handler          # handler of functions
        self.f = self.f_handler.function    # calculated function
        self.dir_minimizer = dir_minimizer  # object used for directional minimizing

        self.start_value = None             # vector of starting value
        self.precision = None               # desired precision

        self.steps = []                     # array storing values of consecutive steps

    def set_function_handler(self, f_handler):
        """Sets reference to function handler allowing to compute functions, e.g. f([x1, x2])"""
        self.f_handler = f_handler
        self.f = self.f_handler.function

    def set_directional_minimizer(self, dir_minimizer):
        """Sets reference to object of directional minimizer class (in our case Golden Section Search)"""
        self.dir_minimizer = dir_minimizer

    def set_parameters(self, start_value, precision):
        """Sets method parameters for starting position of first iteration and searched precision"""
        self.start_value = start_value
        self.steps.append(start_value)
        self.precision = precision

    def get_steps(self):
        """Gets list of arguments values of consecutive algorithm iterations"""
        return self.steps.copy()

    def get_gradient(self, x):
        """Gets gradient from argument tuple x [x1, x2]"""
        val = self.f(x)
        h = 0.000000001
        xh = (x[0] + h, x[1])
        yh = (x[0], x[1] + h)

        gx = (self.f(xh) - val) / h
        gy = (self.f(yh) - val) / h
        return gx, gy

    def get_distance(self, x1, x2):
        if x1 is None or x2 is None:
            return 10e10
        return math.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

    def compute(self):
        """Main computing method"""

        x = self.start_value
        prev_x = None

        # g = self.get_gradient(x)
        # anty_g = -g[0], -g[1]
        # print(anty_g)
        # self.f_handler.set_direction(anty_g)
        # self.f_handler.set_offset(x)
        # minimum = self.dir_minimizer.get_extremum(self.f_handler.directional_function)
        # new_x = (x[0] + minimum*anty_g[0], x[1] + minimum*anty_g[1])
        # self.steps.append(new_x)
        # print("1st iter", new_x)

        while self.get_distance(x, prev_x) > self.precision:
            prev_x = x
            g = self.get_gradient(x)
            anty_g = -g[0], -g[1]
            # print(anty_g)
            self.f_handler.set_direction(anty_g)
            self.f_handler.set_offset(x)
            minimum = self.dir_minimizer.get_extremum(self.f_handler.directional_function)
            x = (x[0] + minimum*anty_g[0], x[1] + minimum*anty_g[1])
            self.steps.append(x)

            print("X", x)

        print(self.steps)


'''
--- EXAMPLE USAGE ---

sdm = SteepestDescentMethod()           # create main object
gss = GoldenSectionSearch()             # create directional minimizer object
gss.set_parameters(-100, 100, 0.001)    # set parameters of directional minimizer

sdm.set_function(lambda x: 2 * (x[0] ** 2) + 3 * (x[1] ** 2))       # pass function that is to be minimized
sdm.set_directional_minimizer(gss)      # pass directional minimizer
sdm.set_parameters([1, 1], 0.001)       # set parameters of the method

sdm.compute()
'''