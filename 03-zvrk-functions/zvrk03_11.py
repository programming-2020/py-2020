zero = 0
one = 1
two = 2
three = 3
five = 5
seven = 7

def first_a(n):
    return n < 0


def second_a(n):
    return n == 0


def check_a(x):
    if(first_a(x)):
        return -one
    elif(second_a(x)):
        return int()
    else:
        return one


def first_b(n):
    return -two < n <= two


def second_b(n):
    return five <= n < seven


def check_b(x):
    if (first_b(x)):
        return two * x
    elif (second_b(x)):
        return three * x - one
    else:
        return one / x


x = float(input('x = '))

print(f'y_a = {check_a(x)}') 
print(f'y_b = {check_b(x)}') 


