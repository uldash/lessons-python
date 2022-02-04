# Заполнение спиралью
# На вход программе подаются два натуральных числа n и m. Напишите
# программу, которая создает матрицу размером n x m заполнив её
# "спиралью" в соответствии с образцом.

# Sample Input 1:
# 4 5
# Sample Output 1:
# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8


def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def right(i, j):
    return i, j + 1


def down(i, j):
    return i + 1, j


def left(i, j):
    return i, j - 1


def up(i, j):
    return i - 1, j


def fill_8_matrix(matrix, n, m):
    index = 1
    direction = ['right', 'down', 'left', 'up']
    current_direction = 0
    x, y = 0, 0

    matrix[x][y] = index
    index += 1
    for k in range(1, n * m):
        # print(direction[current_direction])
        # print_matrix(matrix)
        # input()

        if (direction[current_direction] == 'right' and (y + 1 > m - 1 or matrix[x][y + 1] != 0)) or \
            (direction[current_direction] == 'down' and (x + 1 > n - 1 or matrix[x + 1][y] != 0)) or \
                (direction[current_direction] == 'left' and (y - 1 < 0 or matrix[x][y - 1] != 0)) or \
                    (direction[current_direction] == 'up' and (x - 1 < 0 or matrix[x - 1][y] != 0)):
            current_direction = (current_direction + 1) % 4

        if direction[current_direction] == 'right':
            x, y = right(x, y)
        elif direction[current_direction] == 'down':
            x, y = down(x, y)
        elif direction[current_direction] == 'left':
            x, y = left(x, y)
        elif direction[current_direction] == 'up':
            x, y = up(x, y)

        matrix[x][y] = index
        index += 1
    return 0


def main():
    n, m = [int(i) for i in input().split()]
    matrix = [[0] * m for _ in range(n)]
    fill_8_matrix(matrix, n, m)
    print_matrix(matrix)
    return 0


if __name__ == '__main__':
    main()


# n, m = map(int, input().split())
# i = 1; j = 0; c = 0
# a = [[0] * (100) for _ in range(100)]

# while c < m * n:
#     while a[i][j+1] == 0 and j < m: a[i][j+1] = c+1; j += 1; c += 1
#     while a[i+1][j] == 0 and i < n: a[i+1][j] = c+1; i += 1; c += 1
#     while a[i][j-1] == 0 and j > 1: a[i][j-1] = c+1; j -= 1; c += 1
#     while a[i-1][j] == 0 and i > 1: a[i-1][j] = c+1; i -= 1; c += 1

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(str(a[i][j]).ljust(3), end=' ')
#     print()