'''
Задание 3.

Спросить у пользователя число n.
Напечатать числа от 1 до n. В первой строке - 1 число, во второй - 2 числа, в третьей - 3 и т.д.
'''
number = int(input('Enter a number: '))
count = 1
current_number = 1
line_number = 1
while count <= number:
    print(count, end=" ")
    count += 1
    if current_number == line_number:
        print('\n')
        current_number = 1
        line_number += 1
    else:
        current_number += 1
print('\n')
