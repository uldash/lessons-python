# Напишите программу, которая считывает два целых числа a и b и выводит
# на экран квадрат суммы (a+b)^2 и сумму квадратов a^2+b^2 этих чисел.

# Sample Input 1:
# 3
# 2
# Sample Output 1:
# Квадрат суммы 3 и 2 равен 25
# Сумма квадратов 3 и 2 равна 13

a, b = int(input()), int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a + b)**2)
print('Сумма квадратов', a, 'и', b, 'равна', a**2 + b**2)
