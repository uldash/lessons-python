# На вход программе подается натуральное число n, а затем n целых
# чисел. Напишите программу, которая сначала выводит все отрицательные
# числа, затем нули, а затем все положительные числа, каждое
# на отдельной строке. Числа должны быть выведены в том же порядке,
# в котором они были введены.

nums = [int(input()) for _ in range(int(input()))]

for num in nums:
    if num < 0:
        print(num)
for num in nums:
    if num == 0:
        print(num)
for num in nums:
    if num > 0:
        print(num)