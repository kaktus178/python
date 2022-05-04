"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
решена, например, во фреймворке django.
"""

import os
import shutil
import sys


def add_temp_dir(project='my_project'):
    """
    The function creates duplicates folders and files .html in templates directory
    """
    root_dir = os.path.join(os.getcwd(), project)
    if os.path.isdir(root_dir):
        new_temp_fold = os.path.join(root_dir, 'templates')
        for root, dir, files in os.walk(root_dir):
            if dir != ['templates'] or os.path.join(root, 'templates') == new_temp_fold:
                continue
            temp_fold = os.path.join(root, 'templates')
        for root, dir, files in os.walk(temp_fold):
            for file in files:
                file_root = os.path.join(root, file)
                split_file_root = os.path.split(file_root)
                rel_root = os.path.relpath(split_file_root[0], temp_fold)
                root_new_dir = (os.path.join(new_temp_fold, rel_root))
                if os.path.isdir(root_new_dir):
                    pass
                else:
                    print(os.path.join(new_temp_fold, rel_root))
                    os.makedirs(root_new_dir)
                shutil.copy(file_root, os.path.join(root_new_dir, split_file_root[1]))
    else:
        print('Project not found')


if __name__ == '__main__':
    try:
        name_project = sys.argv[1]
        add_temp_dir(name_project)
    except IndexError:
        add_temp_dir()
        print('Done')
