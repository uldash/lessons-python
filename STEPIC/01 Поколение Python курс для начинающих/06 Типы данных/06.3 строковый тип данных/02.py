# Напишите программу, которая считывает с клавиатуры две строки – имя
# и фамилию пользователя и выводит фразу:

# «Hello [введенное имя] [введенная фамилия]! You just delved
# into Python».

first_name, last_name = input(), input()
print('Hello ' + first_name + ' ' + last_name +
      '! You just delved into Python')
