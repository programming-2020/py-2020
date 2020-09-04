
one = 1
two = 2


def product_while(i):
    n = two * i
    p = one
    while (i <= n):
        p *= i
        i += one
    return p


def product_for(m):
    n = (two * m) + one
    p = one
    for i in range(m, n):
        p *= i
    return p


k = int(input("k = "))

pw = product_while(k)
pf = product_for(k)

message = f'Output_while {pw}; Output_for {pf}'
print(message)
