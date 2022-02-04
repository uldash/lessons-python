# Поворот матрицы
# Напишите программу, которая поворачивает квадратную матрицу чисел
# на 90 градусов по часовой стрелке.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк
# и столбцов в матрице, затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести результат на экран, числа должны
# быть разделены одним пробелом.


def rotate_matrix(matrix, degree):
    n = len(matrix)
    for d in range(degree // 90):
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return 0


def print_matrix(matrix):
    [print(*row) for row in matrix]


n = int(input())
matrix = [[st for st in input().split()] for _ in range(n)]
rotate_matrix(matrix, 90)
print_matrix(matrix)