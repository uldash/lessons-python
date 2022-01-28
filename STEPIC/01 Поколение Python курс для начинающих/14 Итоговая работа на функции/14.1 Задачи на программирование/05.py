# Напишите функцию get_month(language, number), которая принимает
# на вход два аргумента language – язык ru или en и number – номер
# месяца (от 1 до 12) и возвращает название месяца на русском или
# английском языке.


# объявление функции
def get_month(language, number):
    months = [
        'январь',
        'февраль',
        'март',
        'апрель',
        'май',
        'июнь',
        'июль',
        'август',
        'сентябрь',
        'октябрь',
        'ноябрь',
        'декабрь',
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]
    if language == 'ru':
        return months[number - 1]
    else:
        return months[number + 11].lower()


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
