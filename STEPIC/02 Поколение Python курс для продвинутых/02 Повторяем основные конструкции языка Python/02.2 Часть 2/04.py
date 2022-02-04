# Сдвиг в развитии
# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел. Напишите программу
# циклического сдвига элементов списка направо, когда последний
# элемент становится первым, а остальные сдвигаются на одну позицию
# вперед, в сторону увеличения индексов.

numbers = [int(i) for i in input().split()]

# tmp1 = numbers[0]
# for i in range(len(numbers) - 1):
#     tmp2 = numbers[i + 1]
#     numbers[i + 1] = tmp1
#     tmp1 = tmp2
# numbers[0] = tmp1

for i in range(len(numbers) - 1):
    numbers[0], numbers[i + 1] = numbers[i + 1], numbers[0]

print(*numbers)