# Даны две различные клетки шахматной доски. Напишите программу,
# которая определяет, может ли ферзь попасть с первой клетки на вторую
# одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести «YES», если из
# первой клетки ходом ферзя можно попасть во вторую или «NO» в
# противном случае.

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if abs(a2 - a1) == abs(b2 - b1) or a2 == a1 or b2 == b1:
    print('YES')
else:
    print('NO')