"""
Задание 15. Калькулятор в строке.

Пользователь вводит строку вида:
5+3-20*4/2
Необходимо посчитать результат. Для начала, считаем, что приоритета знаков не существует.

Усложнение 1. Приоритет знака все же есть :)

Усложнение 2. В строке пользоваптель может случайно ввести пробелы.

Усложнение 3. В строке могут быть не целые числа...

Усложнение 4. В строке могут быть скобки (разумеется, в первую очередь считается результат в скобках). Глубина вложенности скобок может быть любой )
"""


def pop_operand(string):
    """
    >>> pop_operand('2+10')
    2
    >>> pop_operand('102-10')
    102
    """
    pass


def pop_operator(string):
    """
    >>> string = '+10'
    >>> pop_operator(string)
    '+'
    >>> string == '10'
    True
    """
    operator = string[0]
    if operator == '+' or operator == '-':
        result = string[0]
        string = string[1:]
        return result


def evaluate(first_operand, operator, second_operand):
    """
    >>> evaluate(10, '+', 20)
    30
    >>> evaluate(100, '-', 19)
    81
    """
    if operator == '+':
        return first_operand + second_operand
    elif operator == '-':
        return first_operand - second_operand
    pass


# expression = input('Введите выражение для вычисления:\n')
# result = pop_operand(expression)

# while expression != '':
#     result = evaluate(result, pop_operator(expression), pop_operand(expression))

# print("Result is: ", result)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
