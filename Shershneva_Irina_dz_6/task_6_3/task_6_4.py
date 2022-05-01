"""
Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать
такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг данных из файлов — получить
отдельно фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в какой-нибудь контейнерный
тип (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
"""

import os
import sys
from itertools import zip_longest


def gen_reader(user_pth, hobby_pth):
    with open(user_pth, "r", encoding="utf-8") as user_f, open(hobby_pth, "r", encoding="utf-8") as hobby_f:
        for user, hobby in zip_longest(user_f, hobby_f):
            yield user.removesuffix("\n"), hobby.removesuffix("\n") if hobby else None


def groping(output_pth, user_pth, hobby_pth):
    # test of exists files
    if not (os.path.isfile(user_pth) or
            os.path.isfile(hobby_pth)):
        return -1

    with open(output_pth, "w", encoding="utf-8") as out_file:
        for line in gen_reader(user_pth, hobby_pth):
            print(f"{line[0]}: {line[1]}", file=out_file)

    return 0


if __name__ == "__main__":

    user_name = ""
    hobby_name = ""
    output_name = ""

    if len(sys.argv[1:]) >= 3:
        user_name = sys.argv[1]
        hobby_name = sys.argv[2]
        output_name = sys.argv[3]

    if not user_name:
        user_name = "./users.csv"

    if not hobby_name:
        hobby_name = "./hobby.csv"

    if not output_name:
        output_name = "./out.txt"

    exit(groping(user_pth=user_name, hobby_pth=hobby_name, output_pth=output_name))
