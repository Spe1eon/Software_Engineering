import numpy as np

def check_avg_element(arr):
    avg_value = np.mean(arr)
    return np.any(arr == avg_value)

def elementwise_operation(A, B, result_out):
    np.add(np.sin(np.cos(A, out=result_out)), np.cos(np.sin(B), out=result_out), out=result_out)
    return result_out

def find_matching_row(matrix, v):
    return np.where((matrix == v).all(axis=1))[0]

# Вариант 6. Проверка наличия элемента, равного среднему значению
array_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result_1 = check_avg_element(array_A)

print(result_1, "\n")

# Вариант 12. Поэлементная операция sin(cos(A)) + cos(sin(B))
array_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
array_B = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]], dtype=float)
result_2 = np.empty_like(array_A, dtype=float)
elementwise_operation(array_A, array_B, result_2)

print(result_2, "\n")

# Вариант 24. Поиск строки, совпадающей с вектором v
array_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_B = np.array([4, 5, 6])
result_3 = find_matching_row(array_A, array_B)

if len(result_3) > 0:
    print("Найдена совпадающая строка в индексе:", result_3[0])
else:
    print("Совпадающая строка не найдена.")

