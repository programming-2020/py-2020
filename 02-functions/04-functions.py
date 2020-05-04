

def sum_while(i = 1, n = 10):
    s = 0
    while (i <= n):
        s += i
        i += 1
    return s

def sum_for(m = 1, n = 11):
    s = 0
    for i in range(m, n):
        s += i
    return s

def product_while(i = 1, n = 10):
    p = 1
    while (i <= n):
        p *= i
        i += 1
    return p

def product_for(m = 1, n = 11):
    p = 1
    for i in range(m, n):
        p *= i
    return p

