"""
Задание 6. Построить треугольник Паскаля.

Спросить у пользователя число n.
Напечатать n строк треугольника Паскаля.
Первое и последнее число в строке - 1. Все остальные числа считаются как сумма двух чисел над ней, каждая следующая строка содержит на 1 число больше предыдущей
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
 1 5 10 10 5 1
1 6 15 20 15 6 1
"""


def main():
    print_pascal_triangle()


def print_pascal_triangle():
    number = int(input('Enter a positive number: '))
    pascal_triangle = [[1, 1]]

    while len(pascal_triangle) < number:
        line = [1]
        line_number = len(pascal_triangle)
        while len(line) < line_number + 1:
            line += [pascal_triangle[-1][len(line) - 1] + pascal_triangle[-1][len(line)]]

        line += [1]
        pascal_triangle += [line]

    for line in pascal_triangle:
        print(line)


if __name__ == '__main__':
    from time import clock

    START_TIME = clock()
    main()
    print('\n+===<RUN TIME>===+')
    print('|  %5f.2' % (clock() - START_TIME), 'seconds |')
    print('+==================+')
