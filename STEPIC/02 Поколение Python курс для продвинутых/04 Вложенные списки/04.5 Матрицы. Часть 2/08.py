# На шахматной доске 8 x 8 стоит конь. Напишите программу, которая
# отмечает положение коня на доске и все клетки, которые бьет конь.
# Клетку, где стоит конь, отметьте английской буквой N, клетки,
# которые бьет конь, отметьте символами *, остальные клетки
# заполните точками.
# Sample Input 1:
# b6
# Sample Output 1:

# * . * . . . . .
# . . . * . . . .
# . N . . . . . .
# . . . * . . . .
# * . * . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .


def mark_matrix(matrix, a, b):
    matrix[a][b] = 'N'
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # if (abs(i - a) == 2 and abs(j - b) == 1) or (abs(i - a) == 1
            #                                              and abs(j - b) == 2):
            if abs((i - a) * (j - b)) == 2:
                matrix[i][j] = '*'


def print_matrix(matrix):
    [print(*row) for row in matrix]


n = input()
a, b = 8 - int(n[1]), ord(n[0]) - ord('a')
# print(a, b)
matrix = [['.' for _ in range(8)] for _ in range(8)]
mark_matrix(matrix, a, b)
print_matrix(matrix)