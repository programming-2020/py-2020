zero = 0
one = 1
import math

def sum_a(n):
    s = zero
    f = one
    i = one
    a = zero
    for i in range(i, n + 1):
        f = math.factorial(i)
        a = a + one / (i + one)
        s += f / a
    return s


def sum_b(n):
    s = zero
    f = one
    i = one
    a = zero
    
    for i in range(i, n + 1):
        b = (-one) ** (i-1)
        f = math.factorial(i)
        a += i
        s += b * (a / f)
    return s


def sum_c(n):
    s = one
    i = zero
    sin = zero
    cos = zero
    
    for i in range(i, n + 1):
        sin += math.sin(i)
        cos += math.cos(i)
        s *+ cos / sin
    return s


def sum_d(n):
    s = zero
    i = one
    
    for i in range(i, n + 1):
        b = (-one) ** (i-1)
        s += b * math.factorial(3*i)
    return s


n = int(input("n = "))

message_a = f'Sum_a is: {sum_a(n)}'
print(message_a)

message_b = f'Sum_b is: {sum_b(n)}'
print(message_b)

message_c = f'Sum_c is: {sum_c(n)}'
print(message_c)

message_d = f'Sum_d is: {sum_d(n)}'
print(message_d)