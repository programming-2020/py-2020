# Given points A(xa, yb) and B(xb, yb) are in the same quadrant
# quadrant: I(+, +), II(-, +), III(-, -), IV(+, -)

zero = 0

xa = int(input('xa = '))
ya = int(input('ya = '))

xb = int(input('xb = '))
yb = int(input('yb = '))


quadrant_I = ((xa > zero) and (ya > zero)) and ((xb > zero) and (yb > zero))
quadrant_II = ((xa < zero) and (ya > zero)) and ((xb < zero) and (yb > zero))
quadrant_III = ((xa < zero) and (ya < zero)) and ((xb < zero) and (yb < zero))
quadrant_IV = ((xa > zero) and (ya < zero)) and ((xb > zero) and (yb < zero))


output = quadrant_I or quadrant_II or quadrant_III or quadrant_IV

