"""
* (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а
значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:

  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os
import sys
import json
from collections import defaultdict


def get_data(name_folder='my_project'):
    data_files = defaultdict(list)
    proj_root = os.path.join(os.getcwd(), name_folder)
    for root, dirs, files in os.walk(proj_root):
        n = 0
        for file in files:
            n += 1
            ext = file.rsplit('.', maxsplit=1)[1]
            data_files[str(10 ** len(str(os.stat(os.path.join(root, file)).st_size)))].append(ext)
    result = {}
    for key, value in data_files.items():
        result[key] = (len(value), list(set(value)))
    try:
        with open(f'{name_folder}_summary.json', 'x', encoding='utf-8') as f:
            str_result = json.dumps(result)
            f.write(str_result)
    except FileExistsError:
        print(f'{name_folder}_summary.json already exist')


if __name__ == '__main__':
    try:
        folder = sys.argv[1]
        get_data(folder)
    except IndexError:
        get_data()
