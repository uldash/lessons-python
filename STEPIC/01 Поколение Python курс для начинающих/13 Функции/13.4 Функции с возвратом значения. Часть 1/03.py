# Напишите функцию get_factors(num), принимающую в качестве
# аргумента натуральное число и возвращающую список всех делителей
# данного числа.


def get_factors(num):
    factors = list()
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))