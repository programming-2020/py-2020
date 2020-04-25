

def greather_than(a, b):
    return a > b


def max_value(a, b):
    if (greather_than(a, b)):
        return a
    else:
        return b


def max_message(a, b):
    return f' max = {max_value(a, b)}'


a = int(input('a = '))
b = int(input('b = '))


print(max_message(a, b))
