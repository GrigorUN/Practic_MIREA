import math


def main(x):
    a = math.log10(x ** 3 - x) ** 7
    b = (39 * x ** 2 + 41 + 83 * x) ** 4 / 14 - x ** 2
    r1 = a / b
    a1 = 98 * x ** 3 - x ** 6
    b1 = 97 * (27 * x ** 3 + 42 * x) ** 3 - 47 * x ** 2
    r2 = a1 / b1
    result = r1 + r2
    return result