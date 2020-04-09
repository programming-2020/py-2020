
a = True
b = False

output_a = a or b and not a
output_b = (a or b) and not a

#   True or False -> True
#   not True -> False
#   True and False -> False

# !! python boolean precedence: not, and, or

# not True -> False
# False and False -> False
# True or False -> True

message = f'Output a = {output_a}\nOutput b = {output_b}'
print(message)
