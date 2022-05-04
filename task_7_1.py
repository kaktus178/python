"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os

folder_struct = {
    "my_project": [
        {
            "settings": [{"scripts": [], "bin": []}],
            "mainapp": [],
            "adminapp": [],
            "authapp": []
        }]
}


def project_starter(pth, folder_struct):
    for root, dir in folder_struct.items():
        test_path = os.path.join(pth, root)

        if os.path.exists(test_path):
            pass
        else:
            os.mkdir(test_path)

        if len(dir) > 0:
            for node in dir:
                project_starter(test_path, node)


if __name__ == "__main__":
    project_starter(os.getcwd(), folder_struct)
