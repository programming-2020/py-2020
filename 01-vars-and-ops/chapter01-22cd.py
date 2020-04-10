
number_minus_one = -1
number_one = 1
number_two = 2
number_five = 5

x = float(input("x = "))

first_interval = number_two <= x <= number_five
second_interval = number_minus_one <= x <= number_one

# output = not (( x >= number_two and x <= number_five ) or ( x >= number_minus_one and x <= number_one ))

output_a = first_interval or second_interval
output_b = not (first_interval or second_interval)
output_c = first_interval and second interval


message = f'Output = {}'
print(message)
