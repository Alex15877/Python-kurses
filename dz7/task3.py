import math


def is_prime(num):
    if num % 2 == 0 and num != 2:   # Четные числа, кроме 2 являются непростыми
        return False
    if num == 0 or num == 1:     # Числа 0 и 1 не являются простыми
        return False
    for n in range(3, int(math.sqrt(num)) + 2):
        if num % n == 0:  # Если число делится нацело, то оно непростое
            return False
    return True  # Остальные числа простые


num = int(input('Введите число: '))
tr = is_prime(num)
if tr == True:
    print(f"{num} - это простое число")
else:
    print(f"{num} - это не простое число")