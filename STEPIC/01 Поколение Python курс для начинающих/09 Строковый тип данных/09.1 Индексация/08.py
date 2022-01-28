# На вход программе подается одна строка. Напишите программу,
# которая определяет сколько раз в строке встречаются символы + и *.

s = input()
count_plus = 0
count_asterisk = 0
for i in range(len(s)):
    if s[i] == '+':
        count_plus += 1
    elif s[i] == '*':
        count_asterisk += 1
print(f'Символ + встречается {count_plus} раз')
print(f'Символ * встречается {count_asterisk} раз')
