# optimize body of for loop with minimum multiplication
def exercise():
    """
    >>> exercise()
    40500000000008999995500000
    """
    total = 0
    for n in range(1, 3000000):
        total += (2 * n * n * n + 3 * n * n + 4 * n)
    return total


def solution():
    """
    >>> solution()
    40500000000008999995500000
    """
    total = 0
    for n in range(1, 3000000):
        total += n * (n * (2 * n + 3) + 4)
    return total


# def timer(function):
#     from time import clock
#     from sys  import setrecursionlimit; setrecursionlimit(100)
# # default = 1000
#     startTime = clock()
#
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         return result
#     elapsedTime = round(clock() - startTime, 2)
#     print('-->', function.__name__ + "'s time =", elapsedTime, 'seconds.')
#     return wrapper

if __name__ == "__main__":
    import doctest

    print('answer is =', str(solution()))
    doctest.testmod()
