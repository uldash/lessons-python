# На вход программе подается строка текста в которой буква «h»
# встречается как минимум два раза. Напишите программу, которая
# возвращает исходную строку и переворачивает последовательность
# символов, заключенную между первым и последним вхождением буквы «h».

s = input()

print(s[:s.find('h') + 1] + s[s.rfind('h') - 1:s.find('h'):-1] +
      s[s.rfind('h'):])
