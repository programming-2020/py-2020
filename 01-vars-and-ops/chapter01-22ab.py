number_zero = 0
number_one = 1

x = float(input('x = '))

output_in = (x >= number_zero) and (x <= number_one)
output_out = not output_in

output_in_b = number_zero <= x <= number_one
output_out_b = not output_in_b 

message = f'Output in = {output_in}\nOutput out = {output_out}\n\nOutput in other notation = {output_in_b}\nOutput out other notation = {output_out_b}'
print(message)
