"""
В этом примере рассматриваются документационные строки
"""


def function():
    """
    Строка, стоящая в самом начале функции (а также модуля, класса или метода),
    играет роль особого вида комментариев – документационной строки (docstring).
    """
    print('function called\n\n')


# Вызов функции
function()

# Вывод документационной строки на экран.
# После имени функции нет круглых скобок, поэтому она не вызывается,
# а сама рассматривается как определённый объект
print(function.__doc__)

# Функция help служит для вывода справки
help(function)  # вызов справки по определённой пользователем функции
help(print)  # вызов справки по стандартной функции
