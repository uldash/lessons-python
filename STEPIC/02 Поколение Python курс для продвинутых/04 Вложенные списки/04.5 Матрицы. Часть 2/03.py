# Напишите программу, которая меняет местами столбцы в матрице.
# Формат входных данных
# На вход программе на разных строках подаются два натуральных
# числа n и m — количество строк и столбцов в матрице, затем элементы
# матрицы построчно через пробел, затем числа i и j — номера
# столбцов, подлежащих обмену.


def cols_swap(matrix, first, second):
    for i in range(len(matrix)):
        matrix[i][first], matrix[i][second] = matrix[i][second], matrix[i][
            first]
    return 0


def print_matrix(matrix):
    [print(*rows) for rows in matrix]


n, m = int(input()), int(input())
matrix = [[int(st) for st in input().split()] for _ in range(n)]
i, j = [int(st) for st in input().split()]

cols_swap(matrix, i, j)

print_matrix(matrix)