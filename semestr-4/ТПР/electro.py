from fractions import Fraction

# Исходные данные: матрица оценок альтернатив (10 альтернатив по 4 критериям)
a = [
    [15, 15, 10, 5],
    [10, 5, 10, 5],
    [10, 10, 15, 5],
    [5, 5, 10, 4],
    [5, 15, 5, 3],
    [15, 5, 10, 5],
    [5, 15, 5, 2],
    [15, 5, 15, 5],
    [10, 15, 10, 5],
    [15, 10, 15, 4]
]

# Массив для хранения результатов сравнения альтернатив
b = [' x '] * 10

# Веса критериев
c = [5, 4, 4, 5]

# Инициализация матрицы результатов
for i in range(10):
    b[i] = [' x '] * 10

# Переменные для подсчета количества доминирующих и доминируемых альтернатив
countdominant = 0
countdominanted = 0

# Сравнение альтернатив по критериям и обновление матрицы результатов
for i in range(10):
    for m in range(i + 1, 10):
        for j in range(4):
            if j == 0 or j == 1:
                if a[i][j] < a[m][j]:
                    countdominant += c[j]
                elif a[i][j] > a[m][j]:
                    countdominanted += c[j]
            else:
                if a[i][j] > a[m][j]:
                    countdominant += c[j]
                elif a[i][j] < a[m][j]:
                    countdominanted += c[j]
        if countdominant != 0 and countdominanted == 0:
            b[i][m] = 'inf'
            b[m][i] = ' - '
        elif countdominant == 0 and countdominanted != 0:
            b[m][i] = 'inf'
            b[i][m] = ' - '
        else:
            if countdominant == 0 or countdominanted == 0:
                b[i][m] = ' - '
                b[m][i] = ' - '
            else:
                ratio = countdominant / countdominanted
                if ratio == 1:
                    b[i][m] = ' - '
                    b[m][i] = ' - '
                elif ratio < 1:
                    b[i][m] = ' - '
                    b[m][i] = str(Fraction(1 / ratio).limit_denominator())
                else:
                    b[i][m] = str(Fraction(ratio).limit_denominator())
                    b[m][i] = ' - '
        countdominant = 0
        countdominanted = 0

# Вывод матрицы результатов
for i in b:
    print(i)

# Массив для подсчета количества доминирующих альтернатив для каждой альтернативы
alternative_count = [0] * 10

# Подсчет количества доминирующих альтернатив для каждой альтернативы
for i in range(10):
    for j in range(10):
        if b[i][j] != ' - ' and b[i][j]!= ' x ':
            alternative_count[i] += 1

# Сортировка альтернатив по количеству доминирующих альтернатив
sorted_alternative = sorted(range(len(alternative_count)), key=lambda k: alternative_count[k])

# Вывод лучших альтернатив (наименее подверженных доминированию)
print("\nЛучшие Альтернативы:")
for i in range(10):
    if i == 0:
        print(f"Альтернатива {sorted_alternative[i] + 1}", end="")
    else:
        print(f" <- Алтернатива {sorted_alternative[i] + 1}", end="")
print()
