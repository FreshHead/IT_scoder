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
    pass


def pop_operator(string):
    pass


def evaluate(first_operand, operator, second_operand):
    pass

expression = input('Введите выражение для вычисления:\n')
result = pop_operand(expression)

while expression != '':
    result = evaluate(result, pop_operator(expression), pop_operand(expression))

print("Result is: ", result)
