# Напишите программу, которая проверяет симметричность квадратной
# матрицы относительно главной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и
# столбцов в матрице, затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична
# относительно главной диагонали, и слово NO в противном случае.


def is_symmetry_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


n = int(input())
matrix = [[int(st) for st in input().split()] for _ in range(n)]

if is_symmetry_matrix(matrix):
    print('YES')
else:
    print('NO')