"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
 до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
 * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

minute = 60  # зададим выражения минут, часов и дней в секундах
hour = 3600
day = 86400

duration = int(input('Введите продолжительность в секундах: '))  # задаем duration

if duration < minute:  # вывод информации больше суток года
    print('{} сек'.format(duration))

elif minute <= duration < hour:  # вывод информации до часа
    my_minute = duration // minute
    my_second = duration % minute
    print('{} мин {} сек'.format(my_minute, my_second))

elif hour <= duration < day:  # вывод информации до суток
    my_hour = duration // hour
    duration = duration % hour
    my_minute = duration // minute
    my_second = duration % minute
    print('{} час {} мин {} сек'.format(my_hour, my_minute, my_second))

elif duration >= hour:  # вывод информации больше суток
    my_day = duration // day
    duration = duration % day
    my_hour = duration // hour
    duration = duration % hour
    my_minute = duration // minute
    my_second = duration % minute
    print('дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second))

# h = t // 3600 m = t // 60 % 60 s = t % 60 d = t // 86400 print(f'{d} дн {h} час {m} мин {s} cек')