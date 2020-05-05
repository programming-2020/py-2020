zero = 0
one = 1

def element(n, i ,m):
    return n + i * m

def product_a(n, m):
    p = one
    for i in range(zero, m + one):
        p *= element(n, i, m)
    return p

def product_b(n, m):
    signum = -one
    p = one
    m += 1
    for i in range(one, m):
        p *= n + (signum ** (i + one)) * i * m
    return p
         

n = int(input("n = "))
m = int(input("m = "))

message = f'P {product_b(n, m)}'
print(message)