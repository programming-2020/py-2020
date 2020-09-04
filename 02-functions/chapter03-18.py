# given values a, b and c
# the values represent measurements of triangle
# if triangle can be constructed
# calculate its area sqr(p*(p-a)*(p-b)*(p-c)),
# where p = (a+b+c)/2

from math import sqrt

zero = 0
two = 2


def triangle_check(a, b, c):
    return (a + b) > c


def triangle_p(a, b, c):
    if triangle_check(a, b, c) and triangle_check(a, c, b) and triangle_check(c, b, a):
        return (a + b + c) / two
    return zero


def triangle_area(a, b, c):
    if triangle_p(a, b, c) != zero:
        p = triangle_p(a, b, c)
        return sqrt(p * (p - a) * (p - b) * (p - c))
    return zero


def triangle_message(area):
    if area == zero:
        return "Triangle cannot be constructed"
    return f'Area = {area}'


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

area = triangle_area(a, b, c)
message = triangle_message(area)
print(message)
