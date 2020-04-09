from math import sqrt


print('Point (px, py)')
px = float(input('px = '))
py = float(input('py = '))

ox = 1
oy = 0

r = sqrt(ox ** 2 + oy ** 2)
pr = sqrt((ox - px) ** 2 + (oy - py) ** 2)

output = r <= pr

message = f'Output = {output}'
print(message)
