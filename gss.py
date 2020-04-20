import math


class GoldenSectionSearch:
    def __init__(self, function):
        self.f = function
        self.a = None
        self.b = None

    def set_parameters(self, a, b):
        """Sets parameters for range values"""
        self.a = a
        self.b = b

    def get_extremum(self, f):
        """Gets extremum of given function f"""
        return f(0)
