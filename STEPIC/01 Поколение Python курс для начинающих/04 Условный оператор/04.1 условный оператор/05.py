# Напишите программу, которая определяет, разрешен пользователю
# доступ к интернет-ресурсу или нет.

# Sample Input 1:
# 16
# Sample Output 1:
# Доступ запрещен
# Sample Input 2:
# 18
# Sample Output 2:
# Доступ разрешен

AGE = 18
user_age = int(input())

if user_age < AGE:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')