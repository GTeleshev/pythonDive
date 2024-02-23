# 1. Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

print("Матрица = ", matrix)
print("")
print("Транспонированная матрица = ", transpose_matrix(matrix))
