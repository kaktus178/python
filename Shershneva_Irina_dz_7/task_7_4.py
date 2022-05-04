"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера
файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не
превышает этой границы, но больше предыдущей (начинаем с 0), например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
import sys
import time

size = {}


def scan_mem(pth):
    for root, _, files in os.walk(pth):
        for file in files:
            correct_file = os.path.join(root, file)
            mem = 10 ** len(str(os.stat(correct_file).st_size))
            size[mem] = size.get(mem, 0) + 1


def scan_mem_recursion(pth):
    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:

        for node in files:
            if os.path.isfile(node):
                mem = 10 ** (len(str(os.stat(node).st_size)) - 1)
                size[mem] = size.get(mem, 0) + 1
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()
    print(f"{'soution with os.walk':^39}")
    time_now = time.perf_counter()
    scan_mem(pth)
    print(size, f"\n as {time.perf_counter() - time_now}")

    size = {}
    print(f"{'soution with resursion':^39}")
    time_now = time.perf_counter()
    scan_mem_recursion(pth)
    print(size, f"\n as {time.perf_counter() - time_now}")
