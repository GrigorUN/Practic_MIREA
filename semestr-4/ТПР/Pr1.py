import pandas as pd
import numpy as np

# Создание DataFrame
data = {
    'Вариант решений': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
    'Средний чек (руб.)': [2300, 1800, 1700, 1200, 800, 1950, 500, 2600, 1400, 3500],
    'Удалённость локации (км)': [4.30, 2.30, 2.70, 1.60, 9.30, 2, 11.10, 2.30, 5.80, 3.20],
    'Количество услуг': [16, 17, 20, 13, 8, 16, 4, 22, 16, 19],
    'Рейтинг (от 1 до 5)': [4.80, 5, 4.90, 4.40, 3.80, 5, 2.70, 4.90, 4.80, 4.70]
}

df = pd.DataFrame(data)

# Установка индекса
df.set_index('Вариант решений', inplace=True)

# Переводим критерии в соответствующие веса (больше - лучше)
df['Средний чек (руб.)'] = -df['Средний чек (руб.)']
df['Удалённость локации (км)'] = -df['Удалённость локации (км)']
df['Рейтинг (от 1 до 5)'] = df['Рейтинг (от 1 до 5)']

# Инициализация массива для хранения результатов
pareto_array = np.zeros((10, 10), dtype=object)

# Поиск оптимальных решений методом Парето
for i in range(10):
    for j in range(i+1, 10):
        arr = df.iloc[i].values >= df.iloc[j].values
        check = all(x == True for x in arr)
        arr2 = df.iloc[i].values <= df.iloc[j].values
        check2 = all(x == True for x in arr2)
        if check == True:
            pareto_array[j, i] = df.index[i]
        elif check2 == True:
            pareto_array[j, i] = df.index[j]
        else:
            pareto_array[j, i] = 'н'

pareto_df = pd.DataFrame(pareto_array, columns=df.index)
pareto_df.index = df.index

# Вывод результатов
print("Таблица оптимальных решений по методу Парето:")
print(pareto_df)
