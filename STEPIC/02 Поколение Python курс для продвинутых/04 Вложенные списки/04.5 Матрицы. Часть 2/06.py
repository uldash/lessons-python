# Зеркальное отображение
# Дана квадратная матрица чисел. Напишите программу, которая
# зеркально отображает её элементы относительно
# горизонтальной оси симметрии.


def swap_cols(matrix):
    n = len(matrix)
    for i in range(n // 2):
        matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
    return 0


def print_matrix(matrix):
    [print(*row) for row in matrix]


matrix = [[st for st in input().split()] for _ in range(int(input()))]
swap_cols(matrix)
print_matrix(matrix)