def greather_than(a, b):
    return a > b


def max_value(a, b, c):
    if(greather_than(a, b) and greather_than(a, c)):
        return a
    elif(greather_than(b, a) and greather_than(b, c)):
        return b
    else:
        return c


def max_message(a, b, c):
    return f'max = {max_value(a, b, c)}'


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))


print(max_message(a, b, c))