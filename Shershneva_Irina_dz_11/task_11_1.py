"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных.
"""


class Date:

    @classmethod
    def int_date(cls, day):
        day = day.split('.')
        print(int(day[0]), int(day[1]), int(day[2]))

    @staticmethod
    def valid_date(line):
        line = line.split('.')
        if 1 <= int(line[0]) <= 31 and 1 <= int(line[1]) <= 12 and 1 <= int(line[2]):
            print('Date is correct')
        elif int(line[0]) < 1 or int(line[0]) > 31:
            print('There are no such number of days in this month')
        elif int(line[1]) < 1 or int(line[1]) > 12:
            print('There are no such number of month in a year')
        else:
            print('Error in the year')


day_1 = Date()
day_1.int_date('1.1.2000')
day_1.valid_date('1.1.2000')
day_1.valid_date('0.1.2000')
day_1.valid_date('1.0.2000')
day_1.valid_date('1.1.-2000')
