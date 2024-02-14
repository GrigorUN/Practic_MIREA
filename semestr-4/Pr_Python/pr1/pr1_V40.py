import math


def main(z, x, y):
    z = float(z)
    x = float(x)
    y = float(y)
    a = math.sqrt(x ** 9 + 75 * (z - 1 - 13 * y ** 2) ** 4)
    b = ((math.ceil(z + 19 * z ** 2 + y ** 3)) ** 4) / 86 + x
    c = z ** 6 + 22 * (math.atan(6 + y ** 2 + 64 * x)) ** 3
    res = a + b / c
    return res

