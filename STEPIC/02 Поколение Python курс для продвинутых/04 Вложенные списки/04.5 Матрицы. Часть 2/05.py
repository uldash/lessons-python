# Дана квадратная матрица чисел. Напишите программу, которая меняет
# местами элементы, стоящие на главной и побочной диагонали,
# при этом каждый элемент должен остаться в том же столбце
# (то есть в каждом столбце нужно поменять местами элемент на главной
# диагонали и на побочной диагонали).


def swap_diag(matrix):
    for i in range(len(matrix)):
        matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
    return 0


def print_matrix(matrix):
    [print(*row) for row in matrix]


n = int(input())
matrix = [[int(st) for st in input().split()] for _ in range(n)]
swap_diag(matrix)
print_matrix(matrix)
