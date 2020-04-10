number_zero = 0

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

output_e = (x > number_zero) or (y > number_zero) or (z > number_zero)

output_f = x * y * z > number_zero

output_g = x <= number_zero  and y <= number_zero and z <= number_zero

output_h = (x * y > number_zero) and (x * z > number_zero) and (y * z > number_zero) 

message = f'Output = {output_e}, {output_f}, {output_g}, {output_h}'
print(message)
