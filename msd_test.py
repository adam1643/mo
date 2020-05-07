import unittest
from math import sin, cos, tan, e, pi, exp, log, log2, log10, sqrt
from msd import SteepestDescentMethod
from function_handler import FunctionHandler
from gss import GoldenSectionSearch


class TestFunctionHandler(unittest.TestCase):
    def test_gradient(self):
        fh = FunctionHandler()
        fh.parse_function("x^2+y^2")
        msd = SteepestDescentMethod(None, fh)
        msd.set_function_handler(fh)

        gx, gy = msd.get_gradient((2,2))
        self.assertAlmostEqual(gx, 4, 3)
        self.assertAlmostEqual(gy, 4, 3)

        fh.parse_function("2xy")
        gx, gy = msd.get_gradient((3, 1))
        self.assertAlmostEqual(gx, 2, 3)
        self.assertAlmostEqual(gy, 6, 3)

        fh.parse_function("sin(x) - cos(y)")
        gx, gy = msd.get_gradient((pi, -pi))
        self.assertAlmostEqual(gx, -1, 3)
        self.assertAlmostEqual(gy, 0, 3)

    def test_step(self):
        fh = FunctionHandler()
        fh.parse_function("x^2+y^2-2x")
        # fh.parse_function("-(sin(x^2 + 3y^2) / (0.1 + sqrt(x^2 + y^2)^2) + (x^2 + 5y^2) * (exp(1 - sqrt(x^2 + y^2)^2) / 2))")

        gss = GoldenSectionSearch()
        gss.set_parameters(-100, 100, 0.001)

        msd = SteepestDescentMethod(gss, fh)
        msd.set_function_handler(fh)
        msd.set_parameters((2, 2), 0.1)

        msd.compute()


