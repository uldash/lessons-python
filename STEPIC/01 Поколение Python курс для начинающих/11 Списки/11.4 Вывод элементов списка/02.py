# На вход программе подается натуральное число n, а затем n целых
# чисел. Напишите программу, которая для каждого введенного числа x
# выводит значение функции f(x) = x^2 + 2x + 1, каждое на
# отдельной строке.

n = int(input())
numbers = list()
for _ in range(n):
    numbers.append(int(input()))
print(*numbers, sep='\n')
print()
for x in numbers:
    print(x**2 + 2 * x + 1)
