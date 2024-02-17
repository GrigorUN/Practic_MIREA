import math


def main(m, n, b):
    res = 0
    for k in range(1, b+1):
        for c in range(1, n+1):
            for j in range(1, m+1):
                res += 81 * math.log(5 * j) ** 6 + (
                    69 * j ** 3 - k ** 2 - 60 * c) ** 2
    return res
result = main(6, 8,6)
print(result)