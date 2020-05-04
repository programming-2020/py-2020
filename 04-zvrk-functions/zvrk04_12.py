zero = 0
one = 1

def element(n, i ,m):
    return n + i * m

def product_for_a(n, m):
    p = one
    for i in range(zero, m + 1):
        p *= n + (i * m)
        #p *= element(n, i, m)  moze i ovako!
    return p


def product_while_a(n, m):
    p = one
    i = zero
    while (i <= m):
        p *= n + (i * m)
        i += one
    return p


def product_for_b(n, m):
    p = one
    i = one
    for i in range(i, m + 1):
        p *= n + ((-one) ** (i + 1)) * i ** 2
    return p


def product_while_b(n, m):
    p = one
    i = one
    while (i <= m):
        p *= n + ((-one) ** (i + 1)) * i ** 2
        i += one
    return p


def product_for_c(n, m):
    p = one
    i = one
    for i in range(i, m + 1):
        p *= ((-one) ** (i + 1)) / (n + i ** 2)
    return p


def product_while_c(n, m):
    p = one
    i = one
    while (i <= m):
        p *= ((-one) ** (i + 1)) / (n + i ** 2)
        i += one
    return p


n = int(input("n = "))
m = int(input("m = "))

pfa = product_for_a(n, m)
pwa = product_while_a(n, m)
pfb = product_for_b(n, m)
pwb = product_while_b(n, m)
pfc = product_for_c(n, m)
pwc = product_while_c(n, m)

message_a = f'Output_for_a: {pfa} \nOutput_while_a: {pwa}'
print(message_a)

message_b = f'Output_for_b: {pfb} \nOutput_while_b: {pwb}'
print(message_b)

message_c = f'Output_for_c: {pfc} \nOutput_while_c: {pwc}'
print(message_c)