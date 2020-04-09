from math import factorial

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

output = 1 + x / factorial(2) + y / factorial(3) + z / factorial(4)

message = f'Output = {output}'
print(message)
