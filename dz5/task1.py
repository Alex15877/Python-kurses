# Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем.


def hello():
    name = input("Ввдеите свое имя: ")
    #if type(name) == str:
    if name.isalpha():
        print(f"Приветсвую тебя, {name}!")
    else:
        my_name = "Alex"
        print(f"Привет, меня зовут {my_name}")

hello()