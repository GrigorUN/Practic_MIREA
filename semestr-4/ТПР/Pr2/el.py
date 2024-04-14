a = [
    [15,15,10,5],
    [10,5,10,5],
    [10,10,15,5],
    [5,5,10,4],
    [5,15,5,3],
    [15,5,10,5],
    [5,15,5,2],
    [15,5,15,5],
    [10,15,10,5],
    [15,10,15,4]
]

b = [' x '] * 10

c = [5, 4, 4, 5]

for i in range(10):
    b[i] = [' x '] * 10

countdominant = 0
countdominanted = 0

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
                    b[m][i] = str(round(1 / ratio, 2))
                else:
                    b[i][m] = str(round(ratio, 2))
                    b[m][i] = ' - '
        countdominant = 0
        countdominanted = 0


for i in b:
    print(i)

alternative_count = [0] * 10


for i in range(10):
    for j in range(10):
        if b[i][j] != ' - ' and b[i][j]!= ' x ':
            alternative_count[i] += 1

# Сортировка по количеству вхождений
sorted_alternative = sorted(range(len(alternative_count)), key=lambda k: alternative_count[k])

print("\nЛучшие Альтернативы:")
for i in range(10):
    if i == 0:
        print(f"Альтернатива {sorted_alternative[i] + 1}", end="")
    else:
        print(f" <- Алтернатива {sorted_alternative[i] + 1}", end="")
print()
