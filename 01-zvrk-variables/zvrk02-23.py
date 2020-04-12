print("Start")
print("----")

a = float (input ("a = "))
b = float (input ("b = "))
c = float (input ("c = "))

output_a = (a == b) and (b == c)
message_a = f"Output_a je: {output_a}"
print(message_a)

output_c = (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
message_c = f"Output_c je: {output_c}"
print(message_c)

output_d = (a > 0) and (a <= 100) and (b > 0) and (b <= 100) and (c > 0) and (c <= 100) 
message_d = f"Output_d je: {output_d}"
print(message_d)
print("----")