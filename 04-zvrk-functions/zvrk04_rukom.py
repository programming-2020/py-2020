zero = 0
one = 1
import math

def sum_a(n):
    s = zero
    i = one
    a = zero
    
    for i in range(i, n + 1):
        a = math.sqrt(a + 3)
        s += a
    return s



n = int(input("n = "))

message_a = f'Sum_a is: {sum_a(n)}'
print(message_a)

