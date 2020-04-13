print("Start")
print("----")

a = int (input ("a = "))
b = int (input ("b = "))
c = int (input ("c = "))

output_a = (a < b) and (b < c)
message_a = f"Output_a je: {output_a}"
print(message_a)

output_b = (a > b) and (b > c)
message_b = f"Output_a je: {output_b}"
print(message_b)

output_c = (a >= b) and (b >= c)
message_c = f"Output_c je: {output_c}"
print(message_c)

output_d = (a <= b) and (b <= c) 
message_d = f"Output_d je: {output_d}"
print(message_d)
print("----")