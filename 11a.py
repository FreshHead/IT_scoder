""" Пробую нахождение корня с помощью простого цикла"""
import math


def test_equation(x):
    return 2 * x + 3


def get_length(start, end):
    return end - start


precision = float(input('Введите точность решения:'))
start = -1000
end = 1000
xi = end
yi = math.inf
length = get_length(start, end)

while length > precision:
    print(length, precision)
    temp = test_equation(xi)
    length = length / 2
    if math.fabs(yi) < math.fabs(temp):
        xi -= length
    else:
        xi += length

print(xi)
