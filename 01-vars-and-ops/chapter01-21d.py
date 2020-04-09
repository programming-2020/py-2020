from math import sqrt

n = int(input('n = '))

square_root = sqrt(n)
m = round(square_root)
m **= 2
output = n == m

message = f'Output {output}'
print(message)
