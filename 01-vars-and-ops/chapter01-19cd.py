
a = True
b = False

output_a = not a and b
output_b = not (a and b)

#   True or False -> True
#   not True -> False
#   True and False -> False

# !! python boolean precedence: not, and, or

# not True -> False
# False and False -> False
# True or False -> True

message = f'Output a = {output_a}\nOutput b = {output_b}'
print(message)
