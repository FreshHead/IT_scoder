"""
Задание 7. Знакомимся с массивом.

Создать массив из 10 элементов.
Ввести все 10 штук с клавиатуры.
Посчитать сумму всех элементов, напечатать ее.
"""
import numpy as np

x = np.empty(10)
print(x)

for i in range(len(x)):
    x[i] = int(input('Enter a number: '))

print(x)
total = 0

for element in x:
    total += element

print("Sum of the elements is", total)
