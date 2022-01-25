# Решите уравнение в натуральных числах 28n+30k+31m=365.

for n in range(1, 365 // 28):
    for k in range(1, 365 // 30):
        for m in range(1, 365 // 31):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)
