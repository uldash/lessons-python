# Напишите программу, которая считывает целое число и выводит
# соответствующую ему римскую цифру. Если число находится вне
# диапазона 1-10, то программа должна вывести текст «ошибка».

num = int(input())

if num > 10 or num < 1:
    print('ошибка')
elif num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')
elif num == 5:
    print('V')
elif num == 6:
    print('VI')
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')
elif num == 9:
    print('IX')
elif num == 10:
    print('X')