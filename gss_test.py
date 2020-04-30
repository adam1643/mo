import unittest
from math import sin, cos, tan, e, pi, exp, log, log2, log10, sqrt
from gss import GoldenSectionSearch
from function_handler import FunctionHandler


class TestFunctionHandler(unittest.TestCase):
    def test_parser(self):
        gss = GoldenSectionSearch()
        fh = FunctionHandler()
        fh.set_direction((0, 1))

        fh.parse_function("x")
        gss.set_parameters(0, 3, 0.001)
        self.assertAlmostEqual(gss.get_extremum(fh.directional_function), 0, 2)

        fh.parse_function("x^2")
        gss.set_parameters(-2, 3, 0.001)
        self.assertAlmostEqual(gss.get_extremum(fh.directional_function), 0, 2)

        fh.parse_function("x^2 - 3x")
        gss.set_parameters(-10, 15, 0.001)
        self.assertAlmostEqual(gss.get_extremum(fh.directional_function), 1.5, 2)

        fh.parse_function("1")
        gss.set_parameters(-2, 3, 0.001)
        self.assertAlmostEqual(gss.get_extremum(fh.directional_function), -2, 2)

        fh.parse_function("(-1)*(e^x)")
        gss.set_parameters(-2, 3, 0.001)
        self.assertAlmostEqual(gss.get_extremum(fh.directional_function), 3, 2)
