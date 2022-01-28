# На вход программе подается натуральное число n≥2, а затем n целых
# чисел. Напишите программу, которая создает из указанных чисел
# список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

n = int(input())
lst = list()
first_digit = int(input())
for _ in range(n - 1):
    second_digit = int(input())
    lst.append(first_digit + second_digit)
    first_digit = second_digit
print(lst)
