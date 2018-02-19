"""
Пример того как можно проверить наличие символа s в списке, сете или строке.
"""
s = {'s', 'p', 'a', 'm'}
l = ['s', 'p', 'a', 'm']
string = 'spam'


def lookup(s):
    return 's' in s


print(lookup(s))
print(lookup(l))
print(lookup(string))
