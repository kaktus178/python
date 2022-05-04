"""
* (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os


def make_project(glb_tab, struct, root):

    if glb_tab != -1 and not os.path.exists(root):
        os.mkdir(root)
        print(f"make folder {root}")
    os.chdir(root)
    node_struct = []
    inside_dir = None
    for i, (node_name, line_tab, is_dir) in enumerate(struct):

        if inside_dir:
            if inside_dir[1] < line_tab:
                print(f"in {inside_dir[0]} {node_name}")
                node_struct.append((node_name, line_tab, is_dir))
                if i == len(struct) - 1:
                    make_project(inside_dir[1], node_struct, os.path.join(root, inside_dir[0]))
            elif inside_dir[1] == line_tab and is_dir:
                print(f"put stack in {inside_dir[0]} in {root}")
                make_project(inside_dir[1], node_struct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab)
                node_struct = []
            else:
                print(f"make folder {inside_dir[0]}")

                if not is_dir:
                    node_struct.append((node_name, line_tab, is_dir))

                make_project(inside_dir[1], node_struct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab) if is_dir else None

        elif is_dir:
            print(f"find dir {node_name}")
            inside_dir = (node_name, line_tab)
        else:
            open(node_name, "a").close()
            print(f"create file {node_name} in {root}")


if __name__ == "__main__":
    # image if file not big
    with open("./config.yaml", "r", encoding="utf-8") as conf_text:
        conf = map(lambda x: (
            x.strip().replace("\t", "  ").replace(":", ""),
            x.rstrip().count(" "),
            x.find(":") > 0
        ), conf_text.readlines())

    make_project(-1, list(conf), os.getcwd())

    exit(0)
