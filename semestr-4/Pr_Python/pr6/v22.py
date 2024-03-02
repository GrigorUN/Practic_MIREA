def main(K):
    Oi = {round(K/9) + K for K in K if K < 40 and K >= -77}
    P = {abs(K) for K in K if K < 31 or K >= 1}
    O = {Oi for Oi in Oi if Oi > -52 or Oi < 48}
    A = {P**2 for P in P for P in (-94, 100000000000000)}
    W = {A**2 - A**3 for A in A for A in (-71, 100000000000000)}

    sigma = 0
    for O_val, W_val in zip(O, W):
        sigma += (O_val**3 - W_val % 2)
    u = abs(len(O) == len(W)) - sigma

    return u


print(main({32, 99, -21, -52, -82, -10, 86, 25, 58, -65}))


# def main(K):
#   """
#   Вычисляет и на основе входного множества К.

#   Args:
#     K: Множество целых чисел.

#   Returns:
#     Целое число.
#   """

#   # Вычисление Θ
#   Theta = set(k // 9 + k for k in K if k < 40 and k > -77)

#   # Вычисление P
#   p = set(abs(k) for k in K if (k < 31 or k >= 1))

#   # Вычисление O
#   = set(0 for k in Theta if (k > -52 and k < 48))

#   # Вычисление A
#   A = set(p  2 for p in P if p  2 <= 9400)

#   # Вычисление F
#   F = set(k  2 - k  3 % 2 for k in A)

#   # Вычисление результата
#   result = sum(F)

#   return result


# # Примеры использования
# main({32, 99, -21, 52, 82, -10, 86, 25, 58, 65})  # 5371246
# main({3, -93, 38, 71, 8, -49, -16, 48, -98, 33})  # 1482346
