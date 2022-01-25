# Дано натуральное число. Напишите программу, которая вычисляет:

# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
sum = 0
count = 0
mult = 1
last_digit = num % 10

while num:
    current_digit = num % 10
    first_digit = num
    num = num // 10

    sum += current_digit
    count += 1
    mult *= current_digit

print(sum)
print(count)
print(mult)
print(sum / count)
print(first_digit)
print(first_digit + last_digit)
