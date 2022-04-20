"""Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []
n = int(input('Введите какое количество шуток хотите увидеть: '))
flag = int(input('Если хотите вывести уникальные шутки, введите 1, иначе любой символ: '))


def get_jokes(n, flag):
    """Функция формирования шуток - возвращает n шуток из трёх случайных слов, по одному из каждого списка, заданные\n"
     "    переменные n - какое кол-во шуток хотите увидеть, flag - будут ли слова в каждой шутке повторяться."""
    for i in range(n):
        random_index = choice(nouns)
        random_index_1 = choice(adverbs)
        random_index_2 = choice(adjectives)
        joke = f'{random_index} {random_index_1} {random_index_2}'
        print(joke)
        if flag == 1:
            list_2 = joke.split()
            for noun in nouns:
                for fun in list_2:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)


get_jokes(n, flag)