# Для матрицы A =
# 1 0
# 4 1
# найти A^25


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def mult_matrix(matrix_a, n, m, matrix_b, g, h):
    matrix = [[0] * n for _ in range(h)]
    for i in range(n):
        for j in range(h):
            for k in range(m):
                matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return matrix


def main():
    a = [[1, 0], [4, 1]]
    b = [[1, 0], [4, 1]]
    for _ in range(24):
        b = mult_matrix(b, 2, 2, a, 2, 2)
    print_matrix(b)


if __name__ == '__main__':
    main()