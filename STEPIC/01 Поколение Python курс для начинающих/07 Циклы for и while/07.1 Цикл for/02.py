# Дано предложение и количество раз которое его надо повторить.
# Напишите программу, которая повторяет данное предложение
# нужное количество раз.

text, count = input(), int(input())

for _ in range(count):
    print(text)