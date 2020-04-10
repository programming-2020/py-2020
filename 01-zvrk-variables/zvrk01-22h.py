print("Start")
print("----")

number_zero = 0

x = int (input ("x = "))
y = int (input ("y = "))
z = int (input ("z = "))

output = ((x > number_zero and y <= number_zero and z <= number_zero) or (x <= number_zero and y > number_zero and z <= number_zero) or (x <= number_zero and y <= number_zero and z > number_zero))

message = f"Output = {output}"
print(message)
print("----")