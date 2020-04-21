import math
from gss import GoldenSectionSearch
from parser import Parser


class SteepestDescentMethod:
    def __init__(self, function, dir_minimizer):
        self.f = function                   # calculated function
        self.dir_minimizer = dir_minimizer  # object used for directional minimizing

        self.start_value = None             # vector of starting value
        self.precision = None               # desired precision

        self.steps = []                     # array storing values of consecutive steps

    def set_function(self, function):
        """Sets reference to function allowing to compute f([x1, x2])"""
        self.f = function

    def set_directional_minimizer(self, dir_minimizer):
        """Sets reference to object of directional minimizer class (in our case Golden Section Search)"""
        self.dir_minimizer = dir_minimizer

    def set_parameters(self, start_value, precision):
        """Sets method parameters for starting position of first iteration and searched precision"""
        self.start_value = start_value.copy()
        self.steps.append(start_value.copy())
        self.precision = precision

    def get_steps(self):
        """Gets list of arguments values of consecutive algorithm iterations"""
        return self.steps.copy()

    def compute(self):
        """Main computing method"""
        pass

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