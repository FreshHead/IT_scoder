# optimize body of for loop with minimum multiplication
def exercise():
    total = 0
    for n in range(1, 3000000):
        total += (2 * n * n * n + 3 * n * n + 4 * n)
    print('total =', total)


def solution():
    """
    >>> solution()
    total = 40500000000008999995500000
    """
    total = 0
    for n in range(1, 3000000):
        total += n * (n * (2 * n + 3) + 4)
    print('total =', total)


if __name__ == "__main__":
    import doctest

    doctest.testmod()