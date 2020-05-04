zero = 0
two = 2

one = 1
ten = 10
eleven = 11

def print_while(i = 0, n = 10):
    while i <= n:
        print(i)
        i += 1

def print_for(m = 0, n = 11):
    for i in range(m, n):
        print(i)

# print_while(5, 25)
# print_for()


############################



def odd(n):
    return n % two != zero

def odd_while(i = 1, n = 10):
    while (i <= n):
        if odd(i):
            message = f'Odd {i}'
        else:
            message = f'Even {i}'
        print(message)
        i += 1


def odd_for(m = 1, n = 11):
    for i in range(m, n):
        if odd(i):
            message = f'Odd {i}'
        else:
            message = f'Even {i}'
        print(message)

# odd_while()
# odd_for()

def sum_while(i = 1, n = 10):
    s = 0
    while (i <= n):
        s += i
        i += 1
    return s


sw = sum_while()

def sum_for(m = 1, n = 11):
    s = 0
    for i in range(m, n):
        s += i
    return s

sf = sum_for()

# message = f'Sum while {sw} and sum for {sf}'
# print(message)

def sum_odd_while(i = 1, n = 10):
    s = 0
    while (i <= n):
        if odd(i):
            s += i
        i += 1
    return s

def sum_odd_for(m = 1, n = 11):
    s = 0
    for i in range(m, n):
        if odd(i):
            s += i
    return s

print(sum_odd_while())
print(sum_odd_for())