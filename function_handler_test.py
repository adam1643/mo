import unittest
from math import sin, cos, tan, e, pi, exp, log, log2, log10, sqrt
from function_handler import FunctionHandler


class TestFunctionHandler(unittest.TestCase):
    def test_parser(self):
        fh = FunctionHandler()

        fh.parse_function("sin(x) * x^2")
        self.assertAlmostEqual(fh.function((1, 0)), sin(1))

        fh.parse_function("sqrt(x + y)")
        self.assertAlmostEqual(fh.function((3, 2)), sqrt(3 + 2))

        fh.parse_function("xy")
        self.assertAlmostEqual(fh.function((2, 7)), 2*7)

        fh.parse_function("2x+sin(x)*x^2+3y")
        self.assertAlmostEqual(fh.function((3, 4)), 2*3 + sin(3)*3**2 + 3*4)
