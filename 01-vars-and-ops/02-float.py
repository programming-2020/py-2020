# Example of integer numbers
# + - * -> operators
# / % // -> operators
import math

print("Start")

number_integer = 1
number_float = 1.0

print(type(number_integer))
print(type(number_float))

float_one = 1.0
float_two = 2.0
float_five = 5.0

float_three = float_one + float_two
float_four = float_two * float_two
float_six = (float_one + float_two) * float_two
float_seven = float_three * float_two + float_one

print(float_seven / float_three)
print(round((float_seven / float_three), 2))
print(math.trunc(float_seven / float_three))
print(float_seven // float_three)
print(float_seven % float_three)
