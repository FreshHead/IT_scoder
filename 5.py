"""
Задание 5. Посчитать факториал. Рекурсивно.
Спросить у пользователя число n.
Напечатать n! (факториал числа n).
"""


def factorial(number):
    """
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(6)
    720
    """

    if number > 1:
        return number * factorial(number - 1)
    return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

user_input = int(input('Enter a number: '))
print(factorial(user_input))
