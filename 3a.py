'''
Задание 3.

Спросить у пользователя число n.
Напечатать числа от 1 до n. В первой строке - 1 число, во второй - 2 числа, в третьей - 3 и т.д.
'''
input = int(input('Enter a number: '))
result = ""
count = 1
line_number = 1
while count <= input:
	for i in range(line_number):
		result += ' ' + str(count)
		count += 1
	result += '\n'
	line_number += 1
print(result)
