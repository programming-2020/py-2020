
x = int(input('x'))
y = int(input('y'))
z = int(input('z'))

up_part = x + y - z
down_part = 2 * x + y ** 2 - x * y * z

output = up_part / down_part

message = f'Output = {output}'
print(message)
