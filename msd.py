import math


class SteepestDescentMethod:
    def __init__(self, function, dir_minimizer):
        self.f = function
        self.dir_minimizer = dir_minimizer

        self.start_value = None
        self.precision = None

        self.steps = []

    def set_function(self, function):
        """Sets reference to function allowing to compute f(x1, x2)"""
        self.f = function

    def set_directional_minimizer(self, dir_minimizer):
        """Sets reference to object of directional minimizer class (in our case Golden Section Search)"""
        self.dir_minimizer = dir_minimizer

    def set_parameters(self, start_value, precision):
        """Sets method parameters for starting position of first iteration and searched precision"""
        self.start_value = start_value
        self.precision = precision

    def compute(self):
        pass
