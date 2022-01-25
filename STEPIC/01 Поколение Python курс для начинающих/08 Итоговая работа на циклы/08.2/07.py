# Сриниваса Рамануджан – индийский математик, славившийся своей
# интуицией в области чисел. Когда английский математик Годфри Харди
# навестил его однажды в больнице, он обмолвился, что номером такси,
# на котором он приехал, было 1729, такое скучное и заурядное число.
# На что Рамануджан ответил:
# "Нет, нет! Это очень интересное число. Это наименьшее число,
# выражаемое как сумма двух кубов двумя разными способами".
# Другими словами:
# 1729 = 1^3 + 12^3 = 9^3 + 10^3.

# Напишите программу, которая находит аналогичные интересные числа.
# В ответе запишите первые 5 чисел в порядке возрастания,
# включая число 1729.

# Примечание. Используйте вложенный цикл.

from numba import njit


@njit
def get_result():
    NUM = 33
    for i in range(1, NUM + 1):
        for j in range(1, NUM + 1):
            for m in range(1, NUM + 1):
                for n in range(1, NUM + 1):
                    if i**3 + j**3 == m**3 + n**3 and i != n and i != m and j != n and j != m:
                        print(f'{i} + {j} = {n} + {m} =', i**3 + j**3)


if __name__ == '__main__':
    get_result()
