"""
Задание 12. Работа со строками, или "Ghbdtn!"

Пользователь вводит строку, забыв переключить раскладку на русский язык. Надо перекодировать эту строку и напечатать ее на русском языке.

Усложнение 1. То же самое сделать для английского языка и спросить с какой на какую раскладку перекодироватью.

Усложнение 2. Определить куда перекодировать автоматически.
"""
latin_cyrillic = {
    "q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з", "[": "х", "]": "ъ",
    "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р", "j": "о", "k": "л", "l": "д", ";": "ж", "'": "э",
    "z": "я", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь", ",": "б", ".": "ю"
}

text = input('Введите текст для перевода:')
result_text = ''

for character in text:
    if latin_cyrillic.get(character)is not None:
        result_text += latin_cyrillic.get(character)
    elif character.isupper():
        result_text += latin_cyrillic.get(character.lower()).upper()
    else:
        result_text += character

print(result_text)