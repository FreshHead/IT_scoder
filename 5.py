'''
Задание 5. Посчитать факториал. Рекурсивно.
Спросить у пользователя число n.
Напечатать n! (факториал числа n).
'''
input = int(input('Enter a number: '))


def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    return 1


print(factorial(input))
