import math


def main(z):
    if z < 2:
        return (z ** 2 + 75 * z) ** 7
    elif 2 <= z < 50:
        return ((z - 69 - z ** 3) ** 6 + z ** 2 + 36 * z ** 3)
    else:
        return (68 ** (z ** 3 - 46 * z) ** 4 - (z - z ** 3) ** 5 - 79 * z ** 3)

print(main(147))