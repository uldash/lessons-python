# Две старушки идут навстречу друг другу с постоянными
# скоростями V1 и V2 км/ч. Определите, через какое время старушки
# встретятся, если расстояние между ними равно S км.

# Формат входных данных
# На вход программе подаются три числа с плавающей точкой S, V1, V2,
# каждое на отдельной строке.

s, v1, v2 = float(input()), float(input()), float(input())

v = v1 + v2
t = s / v

print(t)