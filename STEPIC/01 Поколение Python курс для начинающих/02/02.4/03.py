# Напишите программу, вычисляющую объём куба и площадь его полной
# поверхности, по введённому значению длины ребра.

# Sample Input 1:

# 25
# Sample Output 1:

# Объем = 15625
# Площадь полной поверхности = 3750

edge = int(input())

print('Объем =', edge**3)
print('Площадь полной поверхности =', edge**2 * 6)
