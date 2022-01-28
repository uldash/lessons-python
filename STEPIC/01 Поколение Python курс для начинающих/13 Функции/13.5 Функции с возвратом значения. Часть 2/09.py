# Змеиный регистр
# Напишите функцию convert_to_python_case(text), которая принимает в
# качестве аргумента строку в «верблюжьем регистре» и преобразует
# его в «змеиный регистр».


# объявление функции
def convert_to_python_case(text):
    result = text[0].lower()

    for i in range(1, len(text)):
        if text[i].isupper():
            result += '_' + text[i].lower()
        else:
            result += text[i]
    return result


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))