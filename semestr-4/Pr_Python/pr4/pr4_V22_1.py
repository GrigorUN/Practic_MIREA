import math


def main(n):
    if n == 0:
        return -0.01
    return 0.03 + main(n-1) + (
        main(n-1)/64 - (main(n - 1)) ** 3) ** 2