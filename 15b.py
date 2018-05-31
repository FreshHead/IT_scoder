"""
Задание 15. Калькулятор в строке.

1. Делим строку многочлен на одночлены (вместе со знаком)
10 * 2 + 4 - 5 * 2 => 10 * 2 , 4, -5 * 2
2. Заменяем одночлены их решением, если они таковым ещё не являются:
10 * 2 => 20 , 4 => 4, -5 * 2 => -10
3. суммируем одночлены пока не получим окончательное решение:
20 + 4 => 24, 24 + -10 => 14
"""
import re


def evaluate_simple(first_operand, operator, second_operand):
    if operator == '*':
        return float(first_operand) * float(second_operand)
    elif operator == '/':
        return float(first_operand) / float(second_operand)


def evaluate_monomial(monomial):
    if monomial.isdigit():
        return monomial
    operand1 = re.split('[*/]', monomial, 1)[0]
    print(operand1)
    operator = monomial[len(operand1)]
    print(operator)
    operand2 = monomial[len(operand1) + 1:]
    print(operand2)
    return evaluate_simple(operand1, operator, evaluate_monomial(operand2))


def split_by_monomials(expression):
    prepared_expression = expression.replace('-', '+-')
    print(prepared_expression)
    split_monomials = prepared_expression.split('+')
    print(split_monomials)
    total = 0
    for monomial in split_monomials:
        total += float(evaluate_monomial(monomial))
        pass
    print(total)


test_expression = '10*2+4-5*2/4'

split_by_monomials(test_expression)
