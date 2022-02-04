# Латинским квадратом порядка n называется квадратная матрица
# размером n x n, каждая строка и каждый столбец которой содержат
# все числа от 1 до n. Напишите программу, которая проверяет,
# является ли заданная квадратная матрица латинским квадратом.


def transpose_matrix(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[j][i]
    return result


def is_row_squard(matrix):
    n = len(matrix)
    for row in matrix:
        for j in range(n):
            if not j + 1 in row:
                return False
    return True


def is_lat_squard(matrix):
    result = 0
    result += is_row_squard(matrix)
    matrix = transpose_matrix(matrix)
    result += is_row_squard(matrix)

    if result == 2:
        return True
    else:
        return False


def main():
    n = int(input())
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    if is_lat_squard(matrix):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
