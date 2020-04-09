
x = int(input('x = '))
t = int(input('t = '))
y = int(input('y = '))

first = x >= 0
second = t  # False: None, 0, "", '', [], {}, ()
third = x % 2 == 0
fourth = y * y != 4

output = first or second and third or fourth

message = f'Output = {output}'
print(message)
