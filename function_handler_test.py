import unittest
from math import sin, cos, tan, e, pi, exp, log, log2, log10
from function_handler import FunctionHandler


class TestFunctionHandler(unittest.TestCase):
    def test_parser(self):
        fh = FunctionHandler()

        fh.parse_function("sin(x) * x^2")
        self.assertAlmostEqual(fh.function((1, 0)), sin(1))
