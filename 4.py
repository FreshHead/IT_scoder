"""
Задание 4. Посчитать факториал с помощью цикла.

Спросить у пользователя число n.
Напечатать n! (факториал числа n).
"""
number = int(input('Enter a number: '))
result = 1

while input > 0:
    result *= input
    input -= 1

print(result)
