def sum():
    res = a + b
    print("Результат = ", res)

def subtract():
    res = a - b
    print("Результат = ", res)

def multiply():
    res = a * b
    print("Результат = ", res)

def divide():
    res = a / b
    print("Результат = ", res)


while True:
    print("\nПростой калькулятор)\n")
    opr = int(input("Выберите опреацию: 1) +, 2) -, 3) *, 4) /, 5) Закрыть калькулятор: "))
    if opr == 5:
        print("\n    Закрываю калькулятор")
        break
    else:
        a = float(input("Введите первое число:"))
        b = float(input("Введите второе число:"))
        if opr == 1:
            sum()
        elif opr == 2:
            subtract()
        elif opr == 3:
            multiply()
        elif opr == 4:
            if b == 0:
                print("\nНа ноль нельзя делить! \n")
            else:
                divide()
        else:
            print("\nВведите число необходимой операции из списка! \n")
