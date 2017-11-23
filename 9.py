"""
Задание 9. Больше-меньше.

Написать игру - компьютер загадывает число от 1 до 20 (случайное). Наша задача - отгадать. На каждую попытку он отвечает больше ли число загадано, или меньше.
"""
import random as random

number = random.randrange(100) + 1
guess = 0
while guess != number:
    guess = int(input('Введите число от 1 до 100: '))
    if guess > number:
        print('Число ', guess, ' больше загаданного')
    if guess < number:
        print('Число ', guess, ' меньше загаданного')
print('Вы победили!')
