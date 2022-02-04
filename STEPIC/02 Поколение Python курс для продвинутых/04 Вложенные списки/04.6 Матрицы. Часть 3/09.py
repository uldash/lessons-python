# Заполнение диагоналями
# На вход программе подаются два натуральных числа n и m. Напишите
# программу, которая создает матрицу размером n x m заполнив
# её "диагоналями" в соответствии с образцом.

# Sample Input 1:
# 3 5
# Sample Output 1:
# 1  2  4  7  10
# 3  5  8  11 13
# 6  9  12 14 15

# Подсказка: сумма индексов на каждой диагонале равна номеру
# этой диагонали


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def fill_7_matrix(matrix, n, m):
    index = 1
    for k in range(n + m):
        for i in range(n):
            for j in range(m):
                if i + j == k:
                    matrix[i][j] = index
                    index += 1
    return 0



def main():
    n, m = [int(i) for i in input().split()]
    matrix = [[0] * m for _ in range(n)]
    fill_7_matrix(matrix, n, m)
    print_matrix(matrix)


if __name__ == '__main__':
    main()