# Two fields A(xa, ya) and B(xb, yb) are given in the chessboard

# a) are fields A and B the same colour
# b) does the queen in a field A attacks field B
# c) does the knight in a field A attaks field B

two = 2

xa = int(input('xa = '))
ya = int(input('ya = '))

xb = int(input('xb = '))
yb = int(input('yb = '))

black_a = (xa % two == 0) and (ya % two != 0)
black_b = (xb % two == 0) and (ya % two != 0)


output_a = black_a == black_b

