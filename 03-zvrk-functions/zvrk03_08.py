def positive(n):
    return n > 0


def sum(a, b, c):
    s = int()
    if(positive(a)):
        s += a
    if(positive(b)):
        s += b
    if(positive(c)):
        s += c
    return s


def sum_message(a, b, c):
    return f'sum = {sum(a, b, c)}'


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

print(sum_message(a, b, c))