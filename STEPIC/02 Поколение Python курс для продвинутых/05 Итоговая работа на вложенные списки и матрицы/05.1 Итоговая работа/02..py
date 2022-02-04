# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

# Sample Input 1:
# 3
# 1 4 5
# 6 7 8
# 1 1 6
# Sample Output 1:
# 8


def max_number(matrix):
    n = len(matrix)
    largest = matrix[n - 1][n - 1]
    for i in range(n):
        for j in range(n - i - 1, n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
    return largest


def main():
    n = int(input())
    matrix = [[int(el) for el in input().split()] for _ in range(n)]
    print(max_number(matrix))


if __name__ == '__main__':
    main()