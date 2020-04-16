# Frist time input hh:mm:ss
# Second time input hh:mm:ss
# Difference between the to time values 

sixty = 60

ha = int(input("ha = "))
ma = int(input("ma = "))

hb = int(input("hb = "))
mb = int(input("mb = "))

first_time = (ha * sixty) + ma
second_time = (hb * sixty) + mb

difference = second_time - first_time

hours = difference // sixty
minutes = difference % sixty

message = f'Difference is {hours} hours and {minutes} minutes'
print(message)
