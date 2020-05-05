zero = 0
one = 1
import math


def sum(n):
    s = one
    i = one
    
    for i in range(i, n + 1):
        s *= 1 + math.sin(0.1 * i)
    return s

n = int(input("n = "))

message = f'Sum is: {sum(n)}'
print(message)