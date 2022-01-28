# Напишите функцию is_palindrome(text), которая принимает в качестве
# аргумента строку text и возвращает значение True если указанный
# текст является палиндромом и False в противном случае.
# При проверке считайте большие и маленькие буквы одинаковыми,
# а также игнорируйте пробелы, а также символы , . ! ? -.


# объявление функции
def is_palindrome(text):
    tmp_text = ''
    for c in text:
        if c.isalpha():
            tmp_text += c.lower()
    if tmp_text == tmp_text[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))