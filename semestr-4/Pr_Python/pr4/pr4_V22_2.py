def main(n):
    return -0.01 if n == 0 else 0.03 + main(n - 1) + (main(
        n - 1) / 64 - (main(n - 1)) ** 3) ** 2
