# Напишите программу для нахождения цифр четырёхзначного числа.

# Sample Input 1:
# 3281
# Sample Output 1:
# Цифра в позиции тысяч равна 3
# Цифра в позиции сотен равна 2
# Цифра в позиции десятков равна 8
# Цифра в позиции единиц равна 1

num = int(input())

a = (num % 10**1) // 10**0
b = (num % 10**2) // 10**1
c = (num % 10**3) // 10**2
d = (num % 10**4) // 10**3

print('Цифра в позиции тысяч равна', d)
print('Цифра в позиции сотен равна', c)
print('Цифра в позиции десятков равна', b)
print('Цифра в позиции единиц равна', a)