""""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться,
что ничего лишнего не происходит.
"""

import sys
import utils


if __name__ == "__main__":

    args = sys.argv[1:]

    for code in args:
        convertation = utils.currency_rates(code)
        if convertation:
            currency, date = convertation
            date = date.strftime("%d-%m-%Y")
            print(f"{currency}, {date}")