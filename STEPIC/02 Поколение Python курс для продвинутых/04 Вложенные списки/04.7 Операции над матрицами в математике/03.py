# Умножение матриц
# Напишите программу, которая перемножает две матрицы.


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def mult_matrix(matrix_a, matrix_b):
    n = len(matrix_a)
    m = len(matrix_a[0])
    g = len(matrix_b)
    h = len(matrix_b[0])
    result = [[0] * h for _ in range(n)]
    for i in range(n):
        for j in range(h):
            for k in range(m):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def main():
    n, m = [int(i) for i in input().split()]
    matrix_a = [[int(el) for el in input().split()] for _ in range(n)]
    input()
    g, h = [int(i) for i in input().split()]
    matrix_b = [[int(el) for el in input().split()] for _ in range(g)]
    print_matrix(mult_matrix(matrix_a, matrix_b))


if __name__ == '__main__':
    main()
