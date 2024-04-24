def main(K):
    Theta = {k // 9 + k for k in K if k < 40 and k >= -77}
    P = {abs(k) for k in K if k < 31 or k >= 1}
    O_set = {theta for theta in Theta if theta > -52 or theta < 48}
    A = {rho**2 for rho in P if rho > -94}

    Psi = {alpha**2 - alpha**3 for alpha in A if alpha >= -71}

    result = len(O_set.union(Psi)) - sum(
        o**3 - psi % 2 for o in O_set for psi in Psi
    )
    return result


# Примеры использования
print(main({32, 99, -21, -52, -82, -10, 86, 25, 58, -65}))  # 5371246
print(main({3, -93, 38, 71, 8, -49, -16, 48, -98, -33}))  # 1482346
