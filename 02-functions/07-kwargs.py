'''
The syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. 
A double asterisk (**) to unpack dictionaries
'''


def firstFn(first_parameter, **kwargs):
    print(f"First parameter: {first_parameter}")
    print(kwargs)
    for key, value in kwargs.items():
        print(f"key: {key} value: {value}")
    print("Keys only:")
    for key in kwargs.keys():
        print(f"key: {key}")
    print("Values only:")
    for value in kwargs.values():
        print(f"value: {value}")


def secondFn(*args, **kwargs):
    print(f"args = {args}")
    print(f"kwaargs = {kwargs}")


def thirdFn(*args, **kwargs):
    for arg in args:
        print(f"arg {arg}")
    for key, value in kwargs.items():
        print(f"key: {key} value: {value}")


firstFn("String", first="A", second="B", third="C")
