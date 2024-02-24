import math


def main(x):
    res = 0
    n = len(x)
    for i in range(1, n + 1):
        res += (
            math.ceil(
                x[math.ceil(i / 4) - 1] ** 2
                + 58 * x[math.ceil(i / 4) - 1] ** 3
            )
        ) ** 4

    return 10 * res
