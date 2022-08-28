
while True:
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    opr = input("Выберите операцию ( 1. +; 2. -; 3. *; 4. /; 5. **; 6. Выход.) : ")

    try:
        if opr == 1 or opr == "+":
            res = a + b
            print(res)

        elif opr == 2 or opr == "-":
            res = a - b
            print(res)

        elif opr == 3 or opr == "*":
            res = a * b
            print(res)

        elif opr == 4 or opr == "/":
            res = a / b
            print(res)

        elif opr == 5 or opr == "**":
            res = a ** b
            print(res)
        elif opr == 6 or opr == "Выход":
            print("Закрываю калькулятор")
            break
    except:
        print("error\n")