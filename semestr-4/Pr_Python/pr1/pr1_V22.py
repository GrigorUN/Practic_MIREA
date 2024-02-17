import math


def main(x):
    return (math.log10(x ** 3 - x)) ** 7 / (
        (39 * x ** 2 + 41 + 83 * x) ** 4 / 14 - x ** 2) + (
        98 * x ** 3 - x ** 6) / (97 * (
        27 * x ** 3 + 42 * x) ** 3 - 47 * x ** 2)
