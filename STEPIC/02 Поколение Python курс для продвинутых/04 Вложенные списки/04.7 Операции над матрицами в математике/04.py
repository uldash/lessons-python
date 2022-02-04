# Возведение матрицы в степень
# Напишите программу, которая возводит квадратную матрицу в m-ую степень.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и
# столбцов в матрице, затем элементы матрицы, затем натуральное число m.


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


def pow_matrix(matrix, m):
    result = []
    for row in matrix:
        result.append(row)
    for _ in range(m - 1):
        result = mult_matrix(result, matrix)

    return result


def main():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    m = int(input())
    print_matrix(pow_matrix(matrix, m))


if __name__ == '__main__':
    main()
