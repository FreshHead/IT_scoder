"""
Задание 15. Калькулятор в строке.

1. Делим строку многочлен на одночлены (вместе со знаком)
10 * 2 + 4 - 5 * 2 => 10 * 2 , 4, -5 * 2
2. Заменяем одночлены их решением, если они таковым ещё не являются:
10 * 2 => 20 , 4 => 4, -5 * 2 => -10
3. Выполняем действия из массива операторов над одночленами,
пока не получим окончательное решение:
20 + 4 => 24, 24 + -10 => 14
"""


def splitBy

# def calculate(input_string):
#     assert isinstance(input_string, str), "input must be string!"
#     if input_string.isdigit():
#         return float(input_string)
#     # split expression by multiplications and divisions
#     operand = re.split('[*/]', input_string, 1)
#
#
# print(calculate(input('Type a expression:\n')))
