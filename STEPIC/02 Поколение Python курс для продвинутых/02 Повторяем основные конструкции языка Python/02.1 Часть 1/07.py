# Standard American Convention
# На вход программе подаётся натуральное число. Напишите программу,
# которая вставляет в заданное число запятые в соответствии со
# стандартным американским соглашением о запятых в больших числах.

# Формат входных данных
# На вход программе подаётся натуральное число n, (0 < n < 10^100)

# Формат выходных данных
# Программа должна вывести число с запятыми в соответствии с
# условием задачи.

# num = input()
# result = ''
# for i in range(1, len(num) + 1):
#     if i % 3 == 0:
#         result = ',' + num[len(num) - i] + result
#     else:
#         result = num[len(num) - i] + result
# print(result)

num = int(input())
print('{:,}'.format(num))