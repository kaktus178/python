"""
Написать декоратор для логирования типов позиционных аргументов функции, например:

def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5) 5: <class 'int'> Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы
замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:

a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""


def type_logger(func):
    """
    :param func:
    :return: wrapper. showing argument and its types of a function
    """
    print(type(func))

    def type_logger(*args, **kwargs):
        args_and_kwargs = list(args) + list(kwargs.values())
        types = tuple(map(lambda i: f'{i}: {type(i)}', args_and_kwargs))
        print(f'{func.__name__}{types}')
        orig_func = func(*args, **kwargs)
        return orig_func

    return type_logger


@type_logger
def calc_cube(*x, **y):
    """
    :param x:
    :param y:
    :return: calculated cubes of all arguments
    """
    num_list = []
    for el in (*x, *y.values()):
        if isinstance(el, int) or isinstance(el, float):
            num_list.append(el)
    return [i ** 3 for i in num_list]


a = calc_cube(2, 3, 4, 5, vi=6, io=7)
print(a)
