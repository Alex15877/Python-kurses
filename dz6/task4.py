# Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел, которые входят в заданный промежуток.

def recurs_func(n):
    if n <= 1:
        return n
    else:
        return n + recurs_func(n - 1)


number = int(input("Введите число: "))
if number < 0:
    print("!!!")
else:
    print(recurs_func(number))