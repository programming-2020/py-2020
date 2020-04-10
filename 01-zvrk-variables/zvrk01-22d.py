print ("Start")
print("----")

number_minus_one = -1
number_one = 1
number_two = 2
number_five = 5

x = float (input ("x = "))

output = not ( x >= number_two and x <= number_five ) or ( x >= number_minus_one and x <= number_one )

message = f"Output = {output}"
print(message)
print("----")