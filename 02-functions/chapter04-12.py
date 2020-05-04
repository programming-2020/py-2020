zero = 0
one = 1

def element(n, i ,m):
    return n + i * m

def product(n, m):
    p = one
    for i in range(zero, m + one):
        p *= element(n, i, m)
    return p


n = int(input("n = "))
m = int(input("m = "))

message = f'P {product(n, m)}'
print(message)