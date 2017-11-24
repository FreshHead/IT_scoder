"""
Задание 13. Пишем простой архиватор.

Запрашиваем у пользователя строку. В строке могут содержаться повторяющиеся символы, например: аааббввагггг
Заменяем все символы на последовательность: символ+количество повторений. То есть для этой строки будет так: а3б2в2а1г4

Усложнение 1. Пишем декодировщик - на входе пользователь пишет закодированную строку, на выходе - печатаем раскодированную.

Усложнение 2. Спрашиваем кодировать или декодировать строку.

Усложнение 3. Сами определяем - является ли строка корректно закодированной или нет.
"""
# предполагаем, что в строке до 9 повторяющихся символов подряд. Например a1d9s2
digits = '123456789'


def isEncoded(text):
    return text[1] in digits


def decode(text):
    result_string = ''
    for i in range(0, len(text), 2):
        count = int(text[i + 1])
        for j in range(0, count):
            result_string += text[i]

    return result_string


def encode(text):
    result_string = ''
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result_string += text[i - 1] + str(count)
            count = 1
    return result_string + text[i - 1] + str(count)


text = input('Введите текст для архивации/деархивации:\n')
if isEncoded(text):
    print(decode(text))
else:
    print(encode(text))
