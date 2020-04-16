# Given three points A(xa, ya), B(xb, yb), C(xc, yc)
# Do the given dots A, B and C belong to the same line
# y = k*x + n
# y = 2*x + 3

k = 2
n = 3

xa = int(input('xa = '))
ya = int(input('ya = '))

xb = int(input('xb = '))
yb = int(input('yb = '))

xc = int(input('xc = '))
yc = int(input('yc = '))


output = (ya == k * xa + n) and (yb == k * xb + n) and (yc == k * xc + n)

