# Напишите программу проверки симметричности квадратной матрицы
# относительно побочной диагонали.


def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n - i - 1):
            if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
                return False
    return True


def main():
    n = int(input())
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    if is_symmetric(matrix):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()