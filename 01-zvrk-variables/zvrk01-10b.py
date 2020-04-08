print("Start")
print("----")

x = int(input("x = "))
y = int(input("y = "))

#output = ((x * x + y * y) * (x * x + y * y))
#output = (math.ldexp(x, 2) + math.ldexp(y, 2)) nije hteo da importuje math

output = (x**2 + y**2) * (x**2 + y**2)
print("Output = ", output)
print("----")


