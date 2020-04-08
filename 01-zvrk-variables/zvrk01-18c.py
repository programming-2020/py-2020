print("Start")
print("----")

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

output = ( x > y ) or ( y > z ) and not (( x > 0 ) or ( z > x ))
print("Output = ", output)
print("----")