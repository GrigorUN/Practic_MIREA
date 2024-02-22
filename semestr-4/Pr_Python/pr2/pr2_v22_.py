def main(z):
    return (z ** 2 + 75 * z) ** 7 if z < 2 else \
        (68 * (z ** 3 - 46 * z) ** 4 - (
         z - z ** 3) ** 5 - 79 * z ** 3) if z >= 50 else \
        ((z - 69 - z ** 3) ** 6 + z ** 2 + 36 * z ** 3)
