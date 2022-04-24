"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна
возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали
код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре
был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""
import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (currency_code and url):
        return None
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond.ok:
        currency = respond.text.split(currency_code)
        if len(currency) == 1:
            return None
        exchange_value = currency[1].split("</Value>")[0].split("<Value>")[1]
        exchange_value = float(exchange_value.replace(",", "."))
        return exchange_value
    else:
        return None


print((currency_rates("USD")))
print((currency_rates("EUR")))