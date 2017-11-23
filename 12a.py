"""
Смена раскладки теста с помощью функции translate
"""


latin = "qwertyuiop[]asdfghjkl;'zxcvbnm,." + 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>'
cyrillic = "йцукенгшщзхъфывапролджэячсмитьбю" + 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'

latin_cyrillic = str.maketrans(latin, cyrillic)
cyrillic_latin = str.maketrans(cyrillic, latin)


def has_latin_symbols(text):
    for character in text:
        if latin.__contains__(character):
            return True
    return False


def has_cyrillic_symbols(text):
    for character in text:
        if cyrillic.__contains__(character):
            return True
    return False


text = input('Введите текст для перевода:')

if has_latin_symbols(text):
    print(text.translate(latin_cyrillic))
elif cyrillic.__contains__(text[0]):
    print(text.translate(cyrillic_latin))
else:
    print("Невозможно определить раскладку исходного текста")