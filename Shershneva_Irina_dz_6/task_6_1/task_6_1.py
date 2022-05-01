"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

parsed = []
parse_log = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for num, row in enumerate(file):
        raw_row = row.split()
        parse_log = [raw_row[0], raw_row[5][1:], raw_row[6]]
        parsed.append(tuple(parse_log))
        if num == 10:
            break
print(parsed)



