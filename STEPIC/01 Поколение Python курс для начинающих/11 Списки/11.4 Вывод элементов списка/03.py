# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.

# На вход программе подается натуральное число n, а затем n различных
# натуральных чисел. Напишите программу, которая удаляет наименьшее
# и наибольшее значение из указанных чисел, а затем выводит
# оставшиеся числа каждое на отдельной строке, не меняя их порядок.

n = int(input())
numbers = list()
for _ in range(n):
    numbers.append(int(input()))

max_digit = max(numbers)
min_digit = min(numbers)

i = 0
while i < len(numbers):
    if numbers[i] == max_digit or numbers[i] == min_digit:
        del numbers[i]
        continue
    i += 1
print(*numbers, sep='\n')