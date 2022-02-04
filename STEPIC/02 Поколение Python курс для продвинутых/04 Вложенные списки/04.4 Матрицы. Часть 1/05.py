# Напишите программу, которая выводит максимальный элемент в области
# квадратной матрицы, ниже главной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и
# столбцов в матрице, затем элементы матрицы (целые числа)
# построчно через пробел.

# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в
# области квадратной матрицы, ниже главной диагонали.

# Примечание. Элементы главной диагонали также учитываются.


# def get_max(matrix):
#     maximum = matrix[0][0]
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i >= j:
#                 if maximum < matrix[i][j]:
#                     maximum = matrix[i][j]
#     return maximum
def get_max(matrix):
    maximum = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(i + 1):
            if maximum < matrix[i][j]:
                maximum = matrix[i][j]
    return maximum


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

print(get_max(matrix))