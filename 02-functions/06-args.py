'''
The special syntax *argv in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 
*argv is positioned as a last parameter in a function/method or second to last
if the **kwargs is in place.
A single asterisk (*) to unpack iterables.
'''


def firstFn(first_param, *args):
    print(f"First parameter: {first_param}")
    print(args)
    for arg in args:
        print(f"arg in args: {arg}")


firstFn(5)
firstFn(5, 3)
firstFn(5, 6, 2)
firstFn(5, 6, 0, 9, 4, 6)
