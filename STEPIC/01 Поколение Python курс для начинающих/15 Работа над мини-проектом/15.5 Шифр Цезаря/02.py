# На вход программе подается строка текста на английском языке, в
# которой нужно зашифровать все слова. Каждое слово строки следует
# зашифровать с помощью шифра Цезаря (циклического сдвига на длину
# этого слова). Строчные буквы при этом остаются строчными, а
# прописные – прописными.
# Символы, не являющиеся английскими буквами, не изменяются.

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


text = input().split()
result = []
for t in text:
    rot = 0
    for c in t:
        if c.isalpha():
            rot += 1
    result.append(text_transformation('e', 'e', rot, t))

print(*result)
