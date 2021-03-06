# Число словами
# Напишите функцию number_to_words(num), которая принимает в
# качестве аргумента натуральное число num и возвращает его словесное
# описание на русском языке.

# Примечание 1. Считайте, что число 1 ≤ num ≤99.


# объявление функции
def number_to_words(num):
    lst1 = [
        '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь',
        'девять'
    ]
    lst2 = [
        'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
        'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
        'девятнадцать'
    ]
    lst3 = [
        'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
        'семьдесят', 'восемьдесят', 'девяносто'
    ]

    if num < 10:
        return lst1[num]
    if 9 < num < 20:
        return lst2[num - 10]

    result = lst3[num // 10 - 2] + ' ' + lst1[num % 10]
    return result


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))