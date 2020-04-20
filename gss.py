import math


class GoldenSectionSearch:
    def __init__(self):
        self.f = None
        self.a = None
        self.b = None

    def set_function(self, function):
        """Sets reference to function that is to be minimized"""
        self.f = function

    def set_parameters(self, a, b):
        """Sets parameters for range values"""
        self.a = a
        self.b = b

    def get_extremum(self, f):
        """Gets extremum of given function f"""
        return f(0)
