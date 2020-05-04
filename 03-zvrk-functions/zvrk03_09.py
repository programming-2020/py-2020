def isZero(n):
    zero = 0
    return n == zero


def check(a, b, c):
    counter = int()
    if(isZero(a)):
        counter += 1
    if(isZero(b)):
        counter += 1
    if(isZero(c)):
        counter += 1
    return counter


def check_message(a, b, c):
    return f'Values equal zero: {check(a, b, c)}'


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

print(check_message(a, b, c))