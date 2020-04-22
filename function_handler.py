import math
from math import sin, cos, tan, e, pi, exp, log, log2, log10
import ast
import parser


class FunctionHandler:
    def __init__(self):
        self.direction = None

        self.f = None

    def parse_function(self, str_function):
        formula = str_function
        formula = formula.replace('^', '**')
        print(formula)
        self.f = parser.expr(formula).compile()

    def set_direction(self, vector):
        v1, v2 = vector[0], vector[1]
        self.direction = v1 / math.sqrt(v1 ** 2 + v2 ** 2), v2 / math.sqrt(v1 ** 2 + v2 ** 2)

    def function(self, value):
        x, y = value[0], value[1]
        return eval(self.f)

    def directional_function(self, value):
        x1 = value
        x2 = x1 * self.direction[0] / self.direction[1]
        return self.function((x1, x2))


fh = FunctionHandler()
fh.parse_function("math.sin(x)*x^2")
a = fh.function((3, 4))
print(a)
