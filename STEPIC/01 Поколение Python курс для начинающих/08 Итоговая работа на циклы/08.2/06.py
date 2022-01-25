# Дано натуральное число. Напишите программу, которая вычисляет:

# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет,
# то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

n = int(input())

count_3 = 0

last_digit = n % 10
count_last_digit = 0

count_even = 0
sum_more_5 = 0
mult_more_7 = 1
count_0_5 = 0

while n > 0:
    digit = n % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_more_5 += digit
    if digit > 7:
        mult_more_7 *= digit
    if digit == 0 or digit == 5:
        count_0_5 += 1
    n //= 10

print(count_3)
print(count_last_digit)
print(count_even)
print(sum_more_5)
print(mult_more_7)
print(count_0_5)