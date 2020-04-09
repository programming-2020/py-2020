import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
p = int(input('p = '))

output = math.sqrt(p) * math.sqrt(p-b) * (p - a) * (p - c)

message = f'Output = {output}'
print(message)
