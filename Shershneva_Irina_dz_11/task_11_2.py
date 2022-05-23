"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой. """


class CustomException:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def divider(a, b):
    """
    :param a:
    :param b:
    :return: the result of dividing a into b
    """
    try:
        return a / b
    except:
        return f'Input another divider !=0'

print(divider(6, 3))
print(divider(2, 0))
