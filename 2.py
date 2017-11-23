"""
Задание 2.

Спросить у пользователя число n.
Напечатать числа от 1 до n. По 8 штук в строке.
"""
number = int(input('Enter a number: '))
for i in range(number):
    print(i, end = " ")
    if i % 8 == 0:
        print('\n')
print('\n')
