# Three given values a, b, c

# a) are all three values equal
# b) are all three values different
# c) all three values are even numbers
# d) all three values are greather than 0, but not greater than 100

two = 2
zero = 0 
hundred = 100

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

output_a = (a == b) and (a == c) and (b == c)
output_b = (a != b) and (a != c) and (b != c)
output_c = (a % two == zero) and (b % two == zero) and (c % two == zero)
output_d =  (zero < a < hundred) and (zero < b < hundred) and (zero < c < hundred)

