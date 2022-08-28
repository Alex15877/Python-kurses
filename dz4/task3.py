# Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print() выведите на экран прямоугольный треугольник.

size = int(input("Введите размер прямоугольного треугольника: "))
if size < 3:
    print("Вы ввели слишком маленькое число!")
else:
    for i in range(size + 1):
        for j in range(i):
            print("*", end="")

        print()







