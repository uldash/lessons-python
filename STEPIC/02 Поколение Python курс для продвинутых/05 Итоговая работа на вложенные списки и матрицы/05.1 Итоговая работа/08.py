# На вход программе подается натуральное число n. Напишите программу,
# которая создает матрицу размером n x n и заполняет её по
# следующему правилу:

# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, число 1;
# на следующих двух диагоналях число 2, и т.д.

# Sample Input 1:
# 5
# Sample Output 1:
# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0


def print_matrix(matrix):
    [print(*[el for el in row]) for row in matrix]


def fill_matrix(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j - k or i == j + k:
                    matrix[i][j] = k


def main():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]
    fill_matrix(matrix)
    print_matrix(matrix)


if __name__ == '__main__':
    main()