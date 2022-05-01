import sys
import re


def add(arg_price):
    if not arg_price:
        return 1
    with open('bakery.csv', 'a', encoding='utf-8') as file:
        for arg in arg_price[1:]:
            file.write(f'{valid_float_converter(arg):11.2f}\n')
    return 0


def valid_float_converter(value):
    pattern = re.compile(r'\d+(?:[.,]\d+)*$')
    if pattern.match(value):
        return float(value.replace(',', '.'))
    raise ValueError(f'wrong value: {value}')


if __name__ == '__main__':
    try:
        exit(add(sys.argv))
    except ValueError as e:
        print(e)
        exit(1)
