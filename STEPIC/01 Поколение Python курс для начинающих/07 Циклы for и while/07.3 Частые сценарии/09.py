# На вход программе подается натуральное число nn, а затем n
# различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе
# наибольшее число последовательности.

n = int(input())

largest1 = int(input())
largest2 = int(input())

if largest1 > largest2:
    largest1, largest2 = largest2, largest1

for _ in range(n - 2):
    num = int(input())
    if num > largest2:
        largest1 = largest2
        largest2 = num
    elif num > largest1:
        largest1 = num

print(largest2)
print(largest1)
