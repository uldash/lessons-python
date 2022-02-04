# Дан набор точек на координатной плоскости. Необходимо
# подсчитать и вывести количество точек, лежащих в каждой
# координатной четверти.

# Sample Input 1:
# 4
# 0 -1
# 1 2
# 0 9
# -9 -5
# Sample Output 1:

# Первая четверть: 1
# Вторая четверть: 0
# Третья четверть: 1
# Четвертая четверть: 0

n = int(input())
qr1, qr2, qr3, qr4 = 0, 0, 0, 0
for _ in range(n):
    x, y = [int(i) for i in input().split()]
    if x > 0 and y > 0:
        qr1 += 1
    elif x < 0 and y > 0:
        qr2 += 1
    elif x < 0 and y < 0:
        qr3 += 1
    elif x > 0 and y < 0:
        qr4 += 1
print(f'Первая четверть: {qr1}')
print(f'Вторая четверть: {qr2}')
print(f'Третья четверть: {qr3}')
print(f'Четвертая четверть: {qr4}')