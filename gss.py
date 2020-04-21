import math


class GoldenSectionSearch:
    def __init__(self):
        self.precision = None
        self.a = None
        self.b = None

    def set_parameters(self, a, b, precision):
        """Sets parameters for range values and desired precision"""
        self.a = a
        self.b = b
        self.precision = precision

    def get_extremum(self, f):
        """Gets extremum of given function f"""
        return f(0)


'''
--- EXAMPLE USAGE ---

gss = GoldenSectionSearch()             # create directional minimizer object
gss.set_parameters(-100, 100, 0.001)    # set parameters of directional minimizer

f = lambda x: 3*(x**2) + 2*(x)          # test lambda function that is to be minimized
extremum = gss.get_extemum(f)           # compute extremum

'''