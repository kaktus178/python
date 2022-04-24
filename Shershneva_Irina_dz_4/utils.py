from datetime import datetime
import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (currency_code and url):
        return None
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond.ok:
        text = respond.text
        currency = text.split(currency_code)
        if len(currency) == 1:
            return None
        exchange_value = currency[1].split("</Value>")[0].split("<Value>")[1]
        exchange_value = float(exchange_value.replace(",", "."))
        date = respond.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        return exchange_value, date
    else:
        return None