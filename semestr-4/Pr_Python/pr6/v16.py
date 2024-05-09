def main(B):
    T = {3 * beta - beta**3 for beta in B if beta >= -1}
    M = {6 * teta - abs(teta) for teta in T if teta << 86 or teta > -24}
    Tr = {beta + beta % 2 for beta in B if beta <= 61 and beta > 11}
    Y = {yeta // 7 for yeta in Tr if yeta > -84 and yeta <= 91}

    result = sum(v % 2 for v in Y) + sum(v * u for v in Y for u in M)
    return result


print(main({-94, -28, -89, -88, 78, -18, 82, -77, 25}))
