"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:

def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


#>>> a = calc_cube(5)
125
#>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(func):
    """
    val_checker(func)
    :param func:
    :return: wrapper. checks that arguments > 0
    """

    def _val_checker(func2):
        def wrapper(*args, **kwargs):
            for i in args:
                if func(i):
                    print(f'{func2.__name__}: {i} > 0')
                else:
                    raise ValueError(f'wrong value{i}')
            for i in kwargs.values():
                if func(i):
                    print(f'{func2.__name__}: {i} > 0')
                else:
                    raise ValueError(f'wrong value{i}')
            orig_func = func2(*args, **kwargs)
            return orig_func

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
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
