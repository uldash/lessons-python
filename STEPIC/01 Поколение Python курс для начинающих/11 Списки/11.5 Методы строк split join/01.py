# На вход программе подается строка текста. Напишите программу,
# которая выводит слова введенной строки в столбик.

text = input()
print(*text.split(), sep='\n')
