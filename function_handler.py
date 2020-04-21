import math
import ast


class FunctionHandler:
    def __init__(self):
        self.direction = None

    def parse_function(self, str_function):
        pass

    def set_direction(self, vector):
        v1, v2 = vector[0], vector[1]
        self.direction = v1 / math.sqrt(v1 ** 2 + v2 ** 2), v2 / math.sqrt(v1 ** 2 + v2 ** 2)

    def function(self, value):
        x1, x2 = value[0], value[1]
        return 2 * (x1 ** 2) + 3 * (x2 ** 2)

    def directional_function(self, value):
        x1 = value
        x2 = x1 * self.direction[0] / self.direction[1]
        return self.function((x1, x2))
