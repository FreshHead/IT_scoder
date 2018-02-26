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


class Evaluator:
    def __init__(self, expression):
        self.expression = expression

    def pop_operand(self):
        """
        >>> evaluator = Evaluator('102-10')
        >>> evaluator.pop_operand('2+10')
        2
        >>> evaluator.pop_operand('102-10')
        102
        """
        pass

    def pop_operator(self):
        """
        >>> evaluator = Evaluator('+10')
        >>> evaluator.pop_operator()
        '+'
        >>> evaluator.expression == '10'
        True
        """
        operator = self.expression[0]
        if operator == '+' or operator == '-':
            self.expression = self.expression[1:]
            return operator

    def evaluate(self, first_operand, operator, second_operand):
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
