# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит натуральное число из
# отрезка [a; b] с максимальной суммой делителей.

# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных
# пробелом: число с максимальной суммой делителей и сумму его делителей.
# Примечание. Если таких чисел несколько, то выведите наибольшее из них.

a, b = int(input()), int(input())
num = 0
total1 = 0

for i in range(a, b + 1):
    total2 = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total2 += j
        if total2 >= total1:
            total1 = total2
            num = i
print(num, total1)