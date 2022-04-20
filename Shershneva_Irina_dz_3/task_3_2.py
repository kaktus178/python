"""Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
 num_translate("one")
"один"
 num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
 какой тип данных выбрать, в теле функции или снаружи.
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
 num_translate_adv("One")
"Один"
 num_translate_adv("two")
"два"
"""


def num_translate(number):
    print(numbers_dict.get(number))


def num_translate_adv():
    if not new_number[:1].isupper():
        return
    for i in number_eng:
        number_eng[number_eng.index(i)] = number_eng[number_eng.index(i)].capitalize()
    for i in number_rus:
        number_rus[number_rus.index(i)] = number_rus[number_rus.index(i)].capitalize()


new_number = input('Введите название числа на английском от 0 до 10: ')
number_eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Zero', 'One',
              'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
number_rus = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'Ноль',
              'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Десять']

num_translate_adv()
numbers_dict = dict(zip(number_eng, number_rus))
num_translate(new_number)