two = 2

def double(n):
    return two * n

def check_first(a, b, c):
    if a >= b >= c: 
        a = double(a) 
        b = double(b) 
        c = double(c)
    else:
        a = abs(a)
        b = abs(b)
        c = abs(c)
    message = f'a = {a}, b = {b}, c = {c}'
    print(message)

def check_a(a, b, c):
    if a >= b >= c: 
        return double(a)
    else:
        return abs(a)


def check_b(a, b, c):
    if a >= b >= c: 
        return double(b)
    else:
        return abs(b)


def check_c(a, b, c):
    if a >= b >= c: 
        return double(c)
    else:
        return abs(c)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

a = check_a(a, b, c)
b = check_b(a, b, c)
c = check_c(a, b, c)

message = f'a = {a}, b = {b}, c = {c}'
print(message)