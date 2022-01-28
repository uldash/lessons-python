# На вход программе подается строка текста, содержащая различные
# натуральные числа. Из данной строки формируется список чисел.
# Напишите программу, которая меняет местами минимальный и
# максимальный элемент этого списка.

nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

max_digit = max(nums)
max_index = nums.index(max_digit)
min_digit = min(nums)
min_index = nums.index(min_digit)

nums[max_index] = min_digit
nums[min_index] = max_digit

print(*nums)