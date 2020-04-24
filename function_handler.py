import math
from math import sin, cos, tan, e, pi, exp, log, log2, log10, sqrt
import ast
import parser
import numpy as np


class FunctionHandler:
    def __init__(self):
        self.direction = None

        self.f = None

    def parse_function(self, str_function):
        # replace exponents
        formula = str_function.replace('^', '**')

        # add multiplication (*) between numbers and arguments
        formula_as_list = list(formula)
        inserted_stars = 0
        for i in range(len(formula)-1):
            if formula[i] in ['x', 'y'] + [str(i) for i in range(0, 10)] and formula[i+1] in ['x', 'y']:
                formula_as_list.insert(inserted_stars + i + 1, '*')
                inserted_stars += 1
        formula = ''.join(formula_as_list)

        print('Parsed function: f(x) =', formula)
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

    def set_mesh_ranges(self, x1_range, x2_range):
        self.xlist = np.linspace(x1_range[0], x1_range[1], 300)
        self.ylist = np.linspace(x2_range[0], x2_range[1], 400)

    def create_mesh(self):
        X, Y = np.meshgrid(self.xlist, self.ylist)

        values = []
        for a, b in zip(X, Y):
            values.append([])
            for x, y in zip(a, b):
                z = self.function((x, y))
                values[-1].append(z)

        return X, Y, values


fh = FunctionHandler()
fh.parse_function("2x+sin(x)*x^2+3y")
a = fh.function((3, 4))
print(a)
