zero = 0
one = 1
import math


def sum_a(n, x):
    s = zero
    i = one
    p = one
    
    for i in range(i, n + 1):
        p *= math.sin(x)
        s += p
    return s


def sum_b(n, x):
    s = zero
    i = one
    p = one
    
    for i in range(i, n + 1):
        p *= x
        s += math.cos(p)
    return s


def sum_c(n, x):
    s = zero
    i = one
    p = x
    
    for i in range(i, n + 1):
        p = math.sin(p)
        s += p
    return s


n = int(input("n = "))
x = int(input("x = "))

message_a = f'Sum_a is: {sum_a(n,x)}'
print(message_a)

message_b = f'Sum_b is: {sum_b(n,x)}'
print(message_b)

message_c = f'Sum_b is: {sum_c(n,x)}'
print(message_c)