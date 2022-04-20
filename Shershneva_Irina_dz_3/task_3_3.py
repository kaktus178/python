"""Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
 Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""

''' вариант 1
 def thesaurus(*names):
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res

print(thesaurus("Иван", "Мария", "Петр", "Иван", "Ольга", "Иван"))
'''


def thesaurus(*names):
    set_names = {name.title() for name in names}
    first_letter = [name[0].upper() for name in set_names]
    res_dict = {k: list() for k in first_letter}

    for name in set_names:
        res_dict[name[0]].append(name)

    return res_dict


print(thesaurus("Иван", "Мария", "Петр", "Иван", "Ольга", "Иван"))
print(*sorted(thesaurus("Иван", "Мария", "Петр", "Иван", "Ольга", "Иван")))