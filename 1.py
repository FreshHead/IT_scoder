"""
Задание 1.

Спросить у пользователя число n.
Напечатать числа от 1 до n. Через пробел.
"""
number = int(input('Enter a number: '))
for i in range(1, number + 1):
    print(i, end=' ')
