# На вход программе подаются два натуральных числа n и m. Напишите
# программу для создания матрицы размером n х m, заполнив её
# символами . и * в шахматном порядке. В левом верхнем углу должна
# стоять точка. Выведите полученную матрицу на экран, разделяя
# элементы пробелами.


def print_matrix(matrix):
    [print(*row) for row in matrix]


n, m = [int(el) for el in input().split()]
matrix = []
for i in range(n):
    tmp = []
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0:
                tmp.append('.')
            else:
                tmp.append('*')
        else:
            if j % 2 == 0:
                tmp.append('*')
            else:
                tmp.append('.')
    matrix.append(tmp)

print_matrix(matrix)
