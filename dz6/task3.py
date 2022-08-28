# Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну. Определите, сколькими способами можно подняться на заданную ступеньку.

def step_variation(n):
    if n == 1 or n == 2:  # условие выхода
        return 1
    elif n == 0:
        print("Вы сейчас находитесь на нулевой ступеньке!\n")
        return 0
    else:
        return step_variation(n - 1) + step_variation(n - 2)  # рекурсивный вызов


while True:
    try:
        destination_step = int(input("Введите ступеньку на которую хотите подняться: "))
        print(f"Существует {step_variation(destination_step)} способов дойти до нужной ступеньки\n")
    except ValueError:
        print("Нужно вводить число, попробуйте снова.\n")
        break

