zero = 0
one = 1
import math

def sum(n):
    s = one
    i = one
    a = zero
    
    for i in range(i, n + 1):
        a = math.sqrt(a + 2)
        s = s / a
    return s

n = int(input("n = "))

message = f'Sum is: {sum(n)}'
print(message)