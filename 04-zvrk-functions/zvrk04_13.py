zero = 0
one = 1
import math


def sum_factorial(n):
    s = zero
    f = one
    i = one
    for i in range(i, n + 1):
        f = math.factorial(i)
        s += f
    return s


n = int(input("n = "))

message = f'Sum factorial is: {sum_factorial(n)}'
print(message)