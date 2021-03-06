# Переворот числа
# Дано пятизначное или шестизначное натуральное число. Напишите
# программу, которая изменит порядок его последних пяти цифр на
# обратный.

# Формат входных данных
# На вход программе подается одно натуральное пятизначное или
# шестизначное число.

# Формат выходных данных
# Программа должна вывести число, которое получится в результате
# разворота, указанного в условии задачи. Число нужно выводить
# без незначащих нулей.

# num = input()
# if len(num) > 5:
#     print(num[0] + num[-1:-6:-1])
# else:
#     print(num[-1:-6:-1])

num = int(input())
first_digit = 5
result = 0
for i in range(first_digit):
    result += (num % 10) * 10**(first_digit - 1 - i)
    num //= 10
result += num * 10**first_digit
print(result)