# Напишите программу для вычисления суммы двух матриц.


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def sum_matrix(matrix_a, matrix_b, n, m):
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result


def main():
    n, m = [int(i) for i in input().split()]
    matrix_a = [[int(el) for el in input().split()] for _ in range(n)]
    input()
    matrix_b = [[int(el) for el in input().split()] for _ in range(n)]
    print_matrix(sum_matrix(matrix_a, matrix_b, n, m))


if __name__ == '__main__':
    main()
