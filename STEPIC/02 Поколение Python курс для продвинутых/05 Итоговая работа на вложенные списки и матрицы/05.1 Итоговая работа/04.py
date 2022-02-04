# На вход программе подается нечетное натуральное число n. Напишите
# программу, которая создает матрицу размером n x n заполнив её
# символами '.' . Затем заполните символами '*' среднюю строку и
# столбец матрицы, главную и побочную диагональ матрицы.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.


def print_matrix(matrix):
    [print(*row) for row in matrix]


def fill_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == n // 2:
                matrix[i][j] = '*'
                matrix[j][i] = '*'
            if i == n - j - 1 or i == j:
                matrix[i][j] = '*'


def main():
    n = int(input())
    matrix = [['.' for _ in range(n)] for _ in range(n)]

    fill_matrix(matrix)
    print_matrix(matrix)


if __name__ == '__main__':
    main()