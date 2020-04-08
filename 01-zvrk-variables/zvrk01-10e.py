print("Start")
print("----")
import math

p = int(input("p = "))
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

output = math.sqrt(p * ((p - a) * (p - a)) * (p - b) * ((p - c) * (p - c)))
print("Output = ", output)
print("----")