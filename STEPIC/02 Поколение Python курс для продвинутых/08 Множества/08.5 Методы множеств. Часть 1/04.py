# На вход программе подается строка текста, содержащая числа. Для
# каждого числа выведите слово YES (в отдельной строке), если это
# число ранее встречалось в последовательности или NO, если не
# встречалось.
# Sample Input 1:
# 1 1 2 2 5 5 5 5 6 7 8
# Sample Output 1:
# NO
# YES
# NO
# YES
# NO
# YES
# YES
# YES
# NO
# NO
# NO

nmbrs = [int(i) for i in input().split()]
num = set()

for n in nmbrs:
    if n in num:
        print('YES')
    else:
        print('NO')
        num.add(n)
