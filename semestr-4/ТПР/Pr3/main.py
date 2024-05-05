k = [
    [1, 1/3, 4, 7],
    [3, 1, 3, 7],
    [1/4, 1/3, 1, 4],
    [1/7, 1/7, 1/4, 1],
]
a = [
    [1, 1/3, 3, 7],
    [3, 1, 3, 7],
    [1/3, 1/3, 1, 5],
    [1/7, 1/7, 1/5, 1],
]
b = [
    [1, 1/3, 1/2, 3],
    [3, 1, 3, 3],
    [2, 1/3, 1, 4],
    [1/3, 1/3, 1/4, 1],
]
c = [
    [1, 1/3, 3, 1/7],
    [3, 1, 5, 1/3],
    [1/3, 1/5, 1, 1/7],
    [7, 3, 7, 1],
]
d = [
    [1, 3, 1/3, 1],
    [1/3, 1, 1/5, 1/3],
    [3, 5, 1, 3],
    [1, 3, 1/3, 1],
]
def multiply_elements_and_raise(matrix):
    global summ_multiplied_and_raised
    multiplied_and_raised = []
    for row in matrix:
        row_product = 1
        for element in row:
            row_product *= element
        row_result = row_product ** 0.25
        row_result = round(row_result, 3)
        multiplied_and_raised.append(row_result)
        summ_multiplied_and_raised = round(sum(multiplied_and_raised), 3)

    divided_by_sum = []
    for element in multiplied_and_raised:
        division_result = round(element / summ_multiplied_and_raised, 3)
        divided_by_sum.append(division_result)
    return divided_by_sum
result_k = multiply_elements_and_raise(k)
result_a = multiply_elements_and_raise(a)
result_b = multiply_elements_and_raise(b)
result_c = multiply_elements_and_raise(c)
result_d = multiply_elements_and_raise(d)

combined_matrix = [list(row) for row in zip(result_a, result_b, result_c, result_d)]
combined_matrix_transposed = [[combined_matrix[j][i] for j in range(len(combined_matrix))] for i in
                              range(len(combined_matrix[0]))]

array = result_k
array2 = combined_matrix_transposed
import numpy as np

array_np = np.array(array)
array2_np = np.array(array2)

result = np.dot(array_np, array2_np)

print("Результат:")
print("     W1        W2      W3       W4")
print(result)
