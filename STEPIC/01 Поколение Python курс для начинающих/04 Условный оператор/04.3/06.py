# Напишите программу, которая считывает с клавиатуры два целых числа
# и строку. Если эта строка является обозначением одной из четырёх
# математических операций (+, -, *, /), то выведите результат
# применения этой операции к введённым ранее числам, в противном
# случае выведите «Неверная операция». Если пользователь захочет
# поделить на ноль, выведите текст «На ноль делить нельзя!».

a, b, op = int(input()), int(input()), input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/' and b == 0:
    print('На ноль делить нельзя!')
elif op == '/':
    print(a / b)
else:
    print('Неверная операция')