# Задание 4
# Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию, ввести необходимые числа и получить результат.
# Операции, которые необходимо реализовать: сложение, вычитание, умножение, деление, возведение в степень, синус, косинус и тангенс числа.

import math

print("Калькулятор приветствует тебя.")
op = int(input("Выберите номер опреации: 1) +, 2) -, 3) *, 4) /), 5) degree, 6) sin, 7) cos, 8) tg: "))
a = float(input("введите первое число: "))
b = float(input("Введите второе число: "))

if op == 1:
    res = a + b
    print(f"{a} + {b} = {res}.")
elif op == 2:
    res = a - b
    print(f"{a} - {b} = {res}.")
elif op == 3:
    res = a * b
    print(f"{a} умножить на {b} = {res}.")
elif op == 4:
    res = a / b
    print(f"{a} поделить на {b} = {res}.")
elif op == 5:
    res = a ** b
    print(f"{a} в степени {b} = {res}.")
elif op == 6:
    res1 = math.sin(a)
    res2 = math.sin(b)
    print(f"sin числа {a} = {res1},\nsin числа {b} = {res2}.")
elif op == 7:
    res1 = math.cos(a)
    res2 = math.cos(b)
    print(f"cos числа {a} = {res1},\ncos числа {b} = {res2}.")
elif op == 8:
    res1 = math.tan(a)
    res2 = math.tan(b)
    print(f"tg числа {a} = {res1},\ntg числа {b} = {res2}.")
else:
    print("Что то пошло не так")
