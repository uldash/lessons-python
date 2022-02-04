# Квадратная матрица разбивается на четыре четверти, ограниченные
# главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
# Напишите программу, которая вычисляет сумму элементов: верхней
# четверти; правой четверти; нижней четверти; левой четверти.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк
# и столбцов в матрице, затем элементы матрицы (целые числа)
# построчно через пробел.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Элементы диагоналей не учитываются.


def get_sum_quarter(matrix, n, quarter=1):
    sum_quarter = 0
    for i in range(n):
        for j in range(n):
            if quarter == 1:
                if i < j and i < n - 1 - j:
                    sum_quarter += matrix[i][j]
            elif quarter == 2:
                if i < j and i > n - 1 - j:
                    sum_quarter += matrix[i][j]
            elif quarter == 3:
                if i > j and i > n - 1 - j:
                    sum_quarter += matrix[i][j]
            elif quarter == 4:
                if i > j and i < n - 1 - j:
                    sum_quarter += matrix[i][j]
    return sum_quarter


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

print(f'Верхняя четверть: {get_sum_quarter(matrix, n, 1)}')
print(f'Правая четверть: {get_sum_quarter(matrix, n, 2)}')
print(f'Нижняя четверть: {get_sum_quarter(matrix, n, 3)}')
print(f'Левая четверть: {get_sum_quarter(matrix, n, 4)}')