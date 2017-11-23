'''
Задание 2.

Спросить у пользователя число n.
Напечатать числа от 1 до n. По 8 штук в строке.
'''
number = int(input('Enter a number: '))
count = 1
while count <= number:
    print(count, end = " ")
    if count % 8 == 0:
        print('\n')
    count += 1
print('\n')
