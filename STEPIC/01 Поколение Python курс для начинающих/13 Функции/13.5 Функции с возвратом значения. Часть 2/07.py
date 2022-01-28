# BEEGEEK наконец открыл свой банк в котором используются
# специальные банкоматы с необычным паролем.

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и
# c – натуральные числа. Поскольку основатель BEEGEEK фанатеет
# от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в
# качестве аргумента строковое значение пароля password и возвращает
# значение True если пароль является действительным паролем BEEGEEK
# банка и False в противном случае.


# число простое
def is_prime(num):
    num = int(num)
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# число четное
def is_even(num):
    num = int(num)
    return not num % 2


def is_palindrome(num):
    return num == num[::-1]


# объявление функции
def is_valid_password(password):
    text = password.split(':')
    return len(text) == 3 and is_palindrome(text[0]) and is_prime(
        text[1]) and is_even(text[2])


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))