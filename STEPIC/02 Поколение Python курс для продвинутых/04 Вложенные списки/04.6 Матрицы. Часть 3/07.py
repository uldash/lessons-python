# На вход программе подаются два натуральных числа n и m. Напишите
# программу, которая создает матрицу размером n x m заполнив её
# в соответствии с образцом.
# Sample Input 3:
# 3 7
# Sample Output 3:
# 1 2 3 4 5 6 7
# 2 3 4 5 6 7 1
# 3 4 5 6 7 1 2


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def fill_5_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            matrix[i][j] = (j + i) % m + 1


def main():
    n, m = [int(i) for i in input().split()]
    # matrix = [[0 for _ in range(m)] for _ in range(n)]
    matrix = [[0] * m for _ in range(n)]
    fill_5_matrix(matrix, n, m)
    print_matrix(matrix)


if __name__ == '__main__':
    main()