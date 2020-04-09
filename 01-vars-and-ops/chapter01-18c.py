

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

a = x > y
b = y > z
c = x > 0
d = z > x

cd = c or d
cd = not cd
output = a or b and cd

message = f'Output = {output}'
print(message)
