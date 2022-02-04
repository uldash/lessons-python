# Заполнение 2
# На вход программе подаются два натуральных числа n и m. Напишите
# программу, которая создает матрицу размером n x m заполнив её в
# соответствии с образцом.
# Sample Input 1:
# 3 7
# Sample Output 1:
# 1  4  7  10 13 16 19
# 2  5  8  11 14 17 20
# 3  6  9  12 15 18 21


def print_matrix(matrix):
    [print(*[str(cols).ljust(3) for cols in rows]) for rows in matrix]


def fill_matrix(matrix, n, m):
    index = 1
    for i in range(m):
        for j in range(n):
            matrix[j][i] = index
            index += 1


n, m = [int(str) for str in input().split()]

matrix = [[0 for _ in range(m)] for _ in range(n)]

fill_matrix(matrix, n, m)
print_matrix(matrix)