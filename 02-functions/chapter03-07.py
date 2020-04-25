def first(a, b):
    c = int()
    if (a > b):
        c += 1
        return c
    else:
        c += 3
        return c


def second(a, b):
    d = int()
    if (a > b):
        d += 2
        return d
    else:
        d += 4
        return d


def first_message(a, b):
    return f'c = {first(a, b)}\n'


def second_message(a, b):
    return f'd = {second(a, b)}\n'


a = int(input('a = '))
b = int(input('b = '))

print(first_message(a, b))
print(second_message(a, b))
