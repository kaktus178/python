"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
 почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
 Пример:

 email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
 email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
"""

import re

email = input("Input email: ")


def email_parse(email_address):
    """
    :param email_address: string with email address
    :return: return dict with username and domain of an email if it correct
    """
    result_dict = {}
    msg = f'wrong email: {email_address}'
    re_email = re.compile(
        r'^((?<!\.)[A-Za-z0-9!#$%&\'*+/=?^_`{|}~-][A-Za-z0-9!#$%&\'*+./=?^_`{|}~-]*)(?<!\.)@((?<![0-9-])[a-zA-Z]['
        r'a-zA-Z0-9-]*(?<![-])[.][a-zA-Z]+)$')

    if re_email.match(email_address):
        result_dict['username'] = re_email.findall(email_address)[0][0]
        result_dict['domain'] = re_email.findall(email_address)[0][1]
        return result_dict
    else:
        raise ValueError(msg)


print(email_parse(email), '\n')
