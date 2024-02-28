from math import atan, log2


def main(m, n, a, p):
    res1, res2 = 0, 0
    for i in range(1, m + 1):
        res1 += atan(i) ** 4
    for i in range(1, a + 1):
        for c in range(1, n + 1):
            res2 += 70 * i**4 + 83 * c + (log2(p)) ** 6
    return res1 - res2
