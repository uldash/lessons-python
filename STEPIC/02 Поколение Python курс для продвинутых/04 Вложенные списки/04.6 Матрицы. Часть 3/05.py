# # Заполнение 3
# # На вход программе подается натуральное число n. Напишите программу,
# # которая создает матрицу размером n x n заполнив её в
# # соответствии с образцом.
# Sample Input 1:
# 5
# Sample Output 1:
# 1  0  0  0  1
# 0  1  0  1  0
# 0  0  1  0  0
# 0  1  0  1  0
# 1  0  0  0  1


def print_matrix(matrix):
    [print(*[str(cols).ljust(3) for cols in rows]) for rows in matrix]


def fill_matrix(matrix, n):
    for i in range(n):
        matrix[i][i] = 1
        matrix[i][n - i - 1] = 1


n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
fill_matrix(matrix, n)
print_matrix(matrix)
