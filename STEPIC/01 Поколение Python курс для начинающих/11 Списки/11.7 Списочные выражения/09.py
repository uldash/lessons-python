# На вход программе подается строка текста, содержащая целые числа.
# Напишите программу, использующую списочное выражение, которая
# выведет квадраты четных чисел, которые не оканчиваются на цифру 4.

print(*[
    int(str)**2 for str in input().split()
    if int(str) % 2 == 0 and int(str)**2 % 10 != 4
])
