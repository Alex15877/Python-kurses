# Создайте две функции, вычисляющие значения определённых алгебраических выражений. Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.

def funk1(x, y, z):
    print("a + 2b - c")
    # a = float(input("a = "))
    # b = float(input("b = "))
    # c = float(input("c = "))
    res = x + 2 * y - z
    print(res)
    if res <= 5.0 or res <= -5.0:
        for i in range(5, -5, 1):
            print(i, "|")
            if i == res:
                print(res.lower)
    else:
        print("end")



def funk2(x, y, z):
    print("|x| + |y| - z")
    # x = float(input("x = "))
    # y = float(input("y = "))
    # z = float(input("z = "))
    res = abs(x) + abs(y) - z
    print(res)

        # for i in range(5, -5):
        #     step = float(0.5)
        #     i += step
        #     print(i)


#for i in range(-5, 5):


print("Дано два выражения: \n"
      "1) x + 2y - z\n"
      "2) |x| + |y| - z")
formula = int(input("Выберите выражение которое хотите решить: "))
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
if formula == 1:
    funk1(x, y, z)
    # if res <= 5 or res <= -5:
    #     for res in range(5, -5, 1):
    #         print(res, "|")
    # else:
    #     print("end")
    # for i in range(5, -5):
    #     step = float(0.5)
    #     i += step
    #     print(i)
    # print(f"\n {x} + 2*({y}) - {z}")
    # res = x + 2 * y - z
    # print(res)
elif formula == 2:
    print("\n|x| + |y| - z")
    res = abs(x) + abs(y) - z
    print(res)

else:
    print("Ошибка!!!\nВведите 1 или 2 для выбора функции!")

