import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))


up_first = (-1) * b
up_second = math.sqrt((b ** 2) * (-1) * 4 * a * c)

first_part = up_first + (-1) * up_second

second_part = 2 * a

output = first_part / second_part

message = f'Output = {output}'
print(message)
