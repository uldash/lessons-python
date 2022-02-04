# Магический квадрат
# Магическим квадратом порядка n называется квадратная таблица
# размера n x n, составленная из всех чисел 1, 2, 3, ..., n^2 так,
# что суммы по каждому столбцу, каждой строке и каждой из двух
# диагоналей равны между собой. Напишите программу, которая
# проверяет, является ли заданная квадратная матрица
# магическим квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и
# столбцов в матрице, затем элементы матрицы: n строк, по n чисел в
# каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим
# квадратом, и слово NO в противном случае.


def rotate_matrix(matrix, degree):
    n = len(matrix)
    for _ in range(degree // 90):
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return 0


def is_el_sequence(matrix):
    n = len(matrix)
    tmp = []
    for i in range(n):
        tmp.extend(matrix[i])
    for i in range(n**2):
        if not i + 1 in tmp:
            return False
    return True


def is_magik_squard(matrix):

    if not is_el_sequence(matrix):
        return False

    n = len(matrix)
    total = sum(matrix[0])
    s = 0

    for i in range(n):
        if total != sum(matrix[i]):
            return False
    rotate_matrix(matrix, 90)
    for i in range(n):
        if total != sum(matrix[i]):
            return False
    for i in range(n):
        s += matrix[i][i]
    if total != s:
        return False

    s = 0
    for i in range(n):
        s += matrix[i][n - i - 1]
    if total != s:
        return False
    return True


n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
if is_magik_squard(matrix):
    print('YES')
else:
    print('NO')