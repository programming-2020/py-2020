zero = 0
one = 1
ten = 10
eleven = 11

def sum_while(i = one, n = ten):
    s = zero
    while (i <= n):
        s += i
        i += one
    return s

def sum_for(m = one, n = eleven):
    s = zero
    for i in range(m, n):
        s += i
    return s

def product_while(i = one, n = ten):
    p = one
    while (i <= n):
        p *= i
        i += one
    return p

def product_for(m = one, n = eleven):
    p = one
    for i in range(m, n):
        p *= i
    return p

