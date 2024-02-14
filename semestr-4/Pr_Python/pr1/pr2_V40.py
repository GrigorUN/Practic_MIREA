import math


def main(y):
    if y < 126:
        res = y ** 4 + (1 + y ** 2 + y) ** 3
        return res

    if 126 <= y < 220:
        res = (math.sin(y)) ** 6 + 87 * (
            5 * y ** 3) ** 3 + 13 * (math.cos(y - y ** 2)) ** 4
        return res

    if 220 <= y < 277:
        res = y ** 5
        return res

    if 277 <= y < 340:
        res = y
        return res

    if y >= 340:
        res = 61 * y ** 7 + math.log2(y)
        return res

