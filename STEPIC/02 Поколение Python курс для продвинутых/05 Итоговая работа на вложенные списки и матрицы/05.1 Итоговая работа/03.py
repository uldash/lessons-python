# Напишите программу, которая транспонирует квадратную матрицу.
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк
# и столбцов в матрице, затем элементы матрицы.
# Sample Input 1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1:
# 1 4 7
# 2 5 8
# 3 6 9


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def transpose_matrix(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[j][i]
    return result


def main():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    print_matrix(transpose_matrix(matrix))


if __name__ == '__main__':
    main()