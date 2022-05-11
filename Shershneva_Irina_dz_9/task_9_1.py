"""
Создать класс TrafficLight (светофор).

определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""


import time


class TrafficLight:
    def __init__(self):
        self.__color = 'Some color'

    def running(self):
        self.__color = 'Red'
        print(f'{self.__color}', end='')
        for i in range(7):
            time.sleep(1)
            print('.', end='')
        print('')
        self.__color = 'Yellow'
        print(f'{self.__color}', end='')
        for i in range(2):
            time.sleep(1)
            print('.', end='')
        print('')
        self.__color = 'Green'
        print(f'{self.__color}', end='')
        for i in range(2):
            time.sleep(1)
            print('.', end='')
        print('')


traffic = TrafficLight()
traffic.running()

"""
Version 2


import itertools
import time


class TrafficLight:
    def __init__(self):
        self.__color = ['Red', 'Yellow', 'Green']
        self.sec = [7, 2, 2]

    def running(self):
        for color, sec in itertools.zip_longest(self.__color, self.sec):
            print(color)
            time.sleep(sec)


start = TrafficLight()
start.running()
"""