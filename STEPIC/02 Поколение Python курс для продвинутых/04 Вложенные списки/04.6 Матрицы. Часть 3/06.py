# Заполнение 4
# На вход программе подается натуральное число n. Напишите программу,
# которая создает матрицу размером n x n заполнив её в
# соответствии с образцом.
# Sample Input 1:
# 5
# Sample Output 1:
# 1  1  1  1  1
# 0  1  1  1  0
# 0  0  1  0  0
# 0  1  1  1  0
# 1  1  1  1  1


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def fill_4_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            if i <= j and i <= n - 1 - j or i >= j and i >= n - 1 - j:
                matrix[i][j] = 1


def main():
    n = int(input())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    fill_4_matrix(matrix, n)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
