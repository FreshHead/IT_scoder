'''
Задание 2.

Спросить у пользователя число n.
Напечатать числа от 1 до n. По 8 штук в строке. P.S: Cначала собираем строку, потом её выводим. Данный алгоритм оказался быстрее.
'''
number = int(input('Enter a number: '))
result = ""
while number >= 1:
	result = str(number) + ' ' + result
	number -= 1
	if number % 8 == 0:
		result = '\n' + result
print(result)
