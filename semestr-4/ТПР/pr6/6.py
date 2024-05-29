import numpy as np

class VariableValues:
    def __init__(self, values, idx):
        self.values = values
        self.idx = idx

class DeficitResource:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

def extract_c_vector(table):
    return table[0][1:-1]

def transpose_matrix(mat):
    return np.transpose(mat)

def extract_b_vector(table):
    return [row[-1] for row in table[1:-1]]

def extract_a_matrix(table):
    return np.array(table[1:-1, 1:-1])

def extract_cb_vector(table):
    return [row[0] for row in table[1:-1]]

def construct_d_matrix(basis):
    return np.array([item.values for item in basis])

def invert_matrix(mat):
    return np.linalg.inv(mat)

def dot_product(mat1, mat2):
    return np.dot(mat2, mat1)

def calculate_gmin(b, y):
    return np.dot(b, y)

def first_duality_theorem(last_table, basis, b):
    d_matrix = construct_d_matrix(basis)
    d_inv = invert_matrix(d_matrix)
    cb_vector = extract_cb_vector(last_table)
    y_vector = dot_product(d_inv, cb_vector)
    gmin = calculate_gmin(b, y_vector)
    return y_vector, d_inv, gmin

def find_max(plan):
    half_len = len(plan) // 2
    max_val = max(plan[:half_len])
    max_idx = plan.index(max_val)
    return max_val, max_idx

def compute_borders(max_x, a_matrix, b_vector):
    y_vector = []
    for i in range(len(b_vector)):
        product = a_matrix[max_x[1]][i] * max_x[0]
        if product < b_vector[i]:
            y_vector.append(0.0)
        elif product == b_vector[i]:
            y_vector.append(4.0)
    return y_vector

def detect_deficit(y_vector):
    for i, val in enumerate(y_vector):
        if val != 0.0:
            return DeficitResource(val, i)
    print("Дефицитный ресурс не обнаружен!")
    return None

def second_duality_theorem(last_table, a_matrix, b_vector, plan):
    max_x = find_max(plan)
    d_matrix = construct_d_matrix(basis)
    d_inv = invert_matrix(d_matrix)
    cb_vector = extract_cb_vector(last_table)
    y_vector = dot_product(d_inv, cb_vector)
    gmin = calculate_gmin(b_vector, y_vector)
    return detect_deficit(y_vector), gmin

def find_lower_bound(d_matrix, na0, col):
    values = [min(na0) / abs(d_matrix[i][col]) for i in range(len(d_matrix[0])) if d_matrix[i][col] > 0]
    return min(values) if values else np.inf

def find_upper_bound(d_matrix, na0, col):
    values = [max(na0) / abs(d_matrix[i][col]) for i in range(len(d_matrix[0])) if d_matrix[i][col] < 0]
    return max(values) if values else np.inf

def calculate_resource_range(lower_bound, upper_bound, col, b_vector):
    return b_vector[col] - lower_bound, upper_bound + b_vector[col]

def third_duality_theorem(d_matrix, b_vector, a0, y_vector, last_table, deficit_resource, na0):
    print("\n----- Третья теорема двойственности -----\n")

    lower_bounds = []
    upper_bounds = []
    for i in range(len(d_matrix)):
        lower = find_lower_bound(d_matrix, na0, i)
        upper = find_upper_bound(d_matrix, na0, i)
        lower_bounds.append(lower)
        upper_bounds.append(upper)
        print(f"Нижняя граница для ресурса {i + 1} = {lower}")
        print(f"Верхняя граница для ресурса {i + 1} = {upper}")
        x_range = b_vector[i] - lower
        y_range = upper + b_vector[i]
        print(f"Ресурс {i + 1} может изменяться в пределах ({x_range}; {y_range})\n")

    print("\nОценка влияния изменения объема ресурсов на максимальную стоимость продукции:")
    g_max_1 = upper_bounds[0] * y_vector[0]
    print(f"Максимальное значение G для ресурса {deficit_resource.idx + 1} = {upper_bounds[0]} * {y_vector[0]} = {g_max_1}")
    g_max_3 = upper_bounds[2] * y_vector[2]
    print(f"Максимальное значение G для ресурса {deficit_resource.idx + 3} = {upper_bounds[2]} * {y_vector[2]} = {g_max_3}")

    print("\nОптимальное значение целевой функции при максимальном изменении ресурсов:")
    g_max = g_max_1 + g_max_3 + last_table[-1][-1]
    print(f"G_max = {g_max_1} + {g_max_3} + {last_table[-1][-1]} = {g_max}")

def print_simplex_table(table):
    for row in table:
        print(" ".join(f"{cell:10.2f}" for cell in row))
        print("\n")

if __name__ == "__main__":
    f = "400*x1 + 450*x2 + 25*x3 + 300*x4"
    initial_table = np.array([
        [float('inf'), 20.0, 50.0, float('inf')],
        [0.0, 5.0, 20.0, 400.0],
        [0.0, 10.0, 15.0, 450.0],
        [0.0, 0.5, 0.3, 25.0],
        [0.0, 1.0, 2.0, 300]
        [0.0, -20.0, -50.0, 0.0]
    ])

    last_table = np.array([
        [float('inf'), 0, 0, float('inf')],
        [10.0, 0.210, -0.065, 0.65789473684210526315789473684211],
        [0, -0.210, -0.184, 89.8],
        [30.0, -0.052, 0.0788, 9.2105263157894736842105263157895],
        [0, 0.5263, 1.70, 282.894]
    ])

    basis = [
        VariableValues([6.0, 0.0, 5.0], 1),
        VariableValues([2.0, 1.0, 4.0], 4),
        VariableValues([4.0, 0.0, 16.0], 2),
    ]

    plan = [0.0, 0.0, 10, 89.8, 30]
    a0 = [0.65789473684210526315789473684211, 0.0, 9.2105263157894736842105263157895]
    na0 = [50.0, 128.0, 150.0]

    c_vector = extract_c_vector(initial_table)
    print("Вектор C:")
    print(c_vector)

    b_vector = extract_b_vector(initial_table)
    print("Вектор B:")
    print(b_vector)

    a_matrix = extract_a_matrix(initial_table)
    print("Матрица A:")
    print(a_matrix)

    print("Транспонированная матрица A:")
    a_matrix = transpose_matrix(a_matrix)
    print(a_matrix)

    print("Двойственная задача:")
    print(f"g(y) = (b, y) = {f.replace('x', 'y')} -> min")

    print("Ограничения:")
    y_vector, d_matrix_inv, gmin = first_duality_theorem(last_table, basis, b_vector)

    print("\n----- Первая теорема двойственности -----\n")
    print("Матрица Y:")
    print(y_vector)
    print("Матрица D:")
    print(d_matrix_inv)
    print(f"Gmin = (b, y) = {gmin}\n")

    print("\n----- Вторая теорема двойственности -----\n")
    deficit_resource, gmin = second_duality_theorem(last_table, a_matrix, b_vector, plan)
    print(f"Gmin = (b, y) = {gmin}\n")

    third_duality_theorem(d_matrix_inv, b_vector, a0, y_vector, last_table, deficit_resource, na0)
