"""
Задание 3.

Спросить у пользователя число n.
Напечатать числа от 1 до n. В первой строке - 1 число, во второй - 2 числа, в третьей - 3 и т.д.
"""
number = int(input('Enter a number: '))
number_in_line = 1
line_number = 1

for i in range(1, number + 1):
    print(i, end=" ")
    if number_in_line == line_number:
        print('\n')
        number_in_line = 1
        line_number += 1
    else:
        number_in_line += 1

print('\n')
