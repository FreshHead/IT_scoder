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


def evaluate(expression_queue):
    result = expression_queue.pop_operand()
    while expression_queue.expression_string != '':
        result = evaluate_simple(result, expression_queue.pop_operator(), expression_queue.pop_operand())
    return result


def evaluate_simple(first_operand, operator, second_operand):
    """
    >>> evaluate_simple(10, '+', 20)
    30
    >>> evaluate_simple(100, '-', 19)
    81
    """
    if operator == '+':
        return first_operand + second_operand
    elif operator == '-':
        return first_operand - second_operand


class ExpressionQueue:
    def __init__(self, expression_string):
        self.expression_string = expression_string

    def pop_operand(self):
        """
        >>> evaluator = ExpressionQueue('102-10')
        >>> evaluator.pop_operand()
        102
        """
        import re
        operand = re.split('[-+]', self.expression_string, 1)[0]
        self.expression_string = self.expression_string[len(operand):]
        return int(operand)
        pass

    def pop_operator(self):
        """
        >>> expressionQueue = ExpressionQueue('+10')
        >>> expressionQueue.pop_operator()
        '+'
        >>> expressionQueue.expression_string == '10'
        True
        """
        operator = self.expression_string[0]
        if operator == '+' or operator == '-':
            self.expression_string = self.expression_string[1:]
            return operator


print("Result is: ", evaluate(ExpressionQueue(input('Введите выражение для вычисления:\n'))))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
