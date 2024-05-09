import math


def main(z):
    total = 0
    n = len(z)
    for i in range(1, n + 1):
        total += (
            (z[n + 1 - math.ceil(i / 4) - 1]) ** 2 + 90 * z[i-1]**3
        ) ** 4
    return 66 * total

print(main([0.29, 0.15, -0.53, -0.42, 0.68, 0.3, -0.35]))