# Шифр Цезаря


def char_transformation(direction, language, rot, char):
    if direction == 'e':
        d = 1
    else:
        d = -1
    if language == 'e':
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        n = 26
    else:
        if char.isupper():
            start = ord('А')
        else:
            start = ord('а')
        n = 32
    result = chr((ord(char) - start + d * rot) % n + start)
    return result


def text_transformation(direction, language, rot, text):
    result = ''
    for c in text:
        if c.isalpha():
            result += char_transformation(direction, language, rot, c)
        else:
            result += c
    return result


direction = input(
    'Укажите напраление, шифровать/дешифровать (encrypt/decrypt): ').strip()[0]
language = input('Кажите язык алфавита (ru/en): ').strip()[0]
rot = int(input('Укажите шаг сдвига (со сдвигом вправо): ').strip())
text = input('Введите текст: ').strip()

print(text_transformation(direction, language, rot, text))

# for i in range(27):
#     print(text_transformation('d', 'e', i, 'Hawnj pk swhg xabkna ukq nqj.'))
