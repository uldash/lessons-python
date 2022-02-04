# На вход программе подаются два натуральных числа n и m. Напишите
# программу, которая создает матрицу размером n x m и заполняет её
# числами от 1 до n x m в соответствии с образцом.
# Sample Input 1:
# 3 4
# Sample Output 1:
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12


def print_matrix(matrix):
    [print(*[str(col).ljust(3) for col in rows]) for rows in matrix]


def fill_matrix(matrix, n, m):
    index = 1
    for i in range(n):
        for j in range(m):
            matrix[i][j] = index
            index += 1


n, m = [int(i) for i in input().split()]

matrix = [[0 for _ in range(m)] for _ in range(n)]

fill_matrix(matrix, n, m)
print_matrix(matrix)