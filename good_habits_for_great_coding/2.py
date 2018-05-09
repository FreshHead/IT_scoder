import random


def find_random_zeroed(x):
    z = set([number for number in range(1, 100)]) - set(x)
    print(z.pop())


def answer_from_book(x):
    print(5050 - sum(x))


x = random.sample(range(1, 101), 100)
x[random.randint(1, 100)] = 0
print(x)
find_random_zeroed(x)

answer_from_book(x)
