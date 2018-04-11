import random


def find_random_zeroed(x, x_mutated):
    """
    """
    z = set(x) - set(x_mutated)
    print(z)


def answer_from_book(x):
    print(5050-sum(x))

x = random.sample(range(1, 101), 100)
print(x)
y = x.copy()
y[random.randint(1, 100)] = 0
print(y)
find_random_zeroed(x, y)

answer_from_book(y)
