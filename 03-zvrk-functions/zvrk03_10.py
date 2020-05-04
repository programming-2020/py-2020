zero = 0
one = 1
two = 2
three = 3
five = 5

def first(n):
    return n < zero


def second(n):
    return zero <= n < one


def third(n):
    return one <= n < five


def y_value(x):
    if(first(x)):
        return -five
    elif(second(x)):
        return two * x
    elif(third(x)):
        return three * x - one
    else:
        return two * x


x = int(input('x = '))
print(f'y = {y_value(x)}')