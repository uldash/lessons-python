# На вход программе подаются два натуральных числа n и m. Напишите 
# программу, которая создает матрицу размером n x  m заполнив 
# её "змейкой" в соответствии с образцом.
# Sample Input 1:
# 3 5
# Sample Output 1:
# 1  2  3  4  5
# 10 9  8  7  6
# 11 12 13 14 15

def print_matrix(matrix):
    [print(*[str(el).ljust(3) for el in row]) for row in matrix]


def fill_6_matrix(matrix, n, m):
    counter = 1
    for i in range(n):
        for j in range(m):
            if i % 2 != 0:
                matrix[i][m - j - 1] = counter
            else:
                matrix[i][j] = counter
            counter += 1


def main():
    n, m = [int(i) for i in input().split()]
    matrix = [[0] * m for _ in range(n)]
    fill_6_matrix(matrix, n, m)
    print_matrix(matrix)
    return 0


if __name__ == '__main__':
    main()
