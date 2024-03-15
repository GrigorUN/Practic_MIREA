# def main(K):
#     Theta = {k // 9 + k for k in K if -77 <= k < 40}
#     P = {abs(k) for k in K if k < 31 or k >= 1}
#     eto_O = {theta for theta in Theta if theta > -52 or theta < 48}
#     Psi = {alpha**2 - alpha**3 for alpha in P if -71 <= alpha < float("inf")}

#     v = len(eto_O.union(Psi)) - sum(
#         (eto_O**3 - psi % 2) for eto_O in eto_O for psi in Psi
#     )

#     return v


# Примеры использования:
result1 = main({32, 99, -21, -52, -82, -10, 86, 25, 58, -65})
print("main({32, 99, -21, -52, -82, -10, 86, 25, 58, -65}) =", result1)

result2 = main({3, -93, 38, 71, 8, -49, -16, 48, -98, -33})
print("main({3, -93, 38, 71, 8, -49, -16, 48, -98, -33}) =", result2)
