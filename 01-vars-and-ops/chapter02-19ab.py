# a) Value is true if given measurements can construct a triangle.
# b) Valuse is true if one rectangle can be placed into another,
#	provided that their sides are parallel.


# a)
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

first_condition = x + y < z
second_condition = x + z < y
third_condition = z + y < x

output_a = first_condition and second_condition and third_condition


# b)
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

fourth_condition = (c < a) and (c < b)
fifth_condition = (d < a) and (d < b)

output_b = fourth_condition and fifth_condition


