"""
* (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее,
чем может сначала показаться.
"""


def get_sign(x):
    if x[0] in '+-':
        return x[0]


list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(list_1):
    sign = get_sign(list_1[i])
    if list_1[i].isdigit() or (sign and list_1[i][1:].isdigit()):
        if sign:
            list_1[i] = sign + list_1[i][1:].zfill(2)
        else:
            list_1[i] = list_1[i].zfill(2)

        list_1.insert(i, '"')
        list_1.insert(i + 2, '"')
        i += 2

    i += 1

message = ' '.join(list_1)
print(message)