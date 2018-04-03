#!/usr/bin/python


def power(b, exp):
    """
    >>> power(2, 2)
    4
    >>> power(127, 1)
    127
    >>> pow(124,28)
    41286416034183357627293244490549811095105513401293656293376
    """
    binary_string = str(bin(exp))[2:]
    reversed_string = reversed(binary_string)
    product = 1
    for ch in reversed_string:
        if ch == '1':
            product *= b
        b *= b
    return product

