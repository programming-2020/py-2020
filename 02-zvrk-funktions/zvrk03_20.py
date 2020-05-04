
zero = 0

def check(a):
    return a != 0


def my_function(a, b):
    if check(a):
        return -(b / a)
    return zero


def message(a, b):
    x = my_function(a, b)
    if x != 0:
        return f"x = {x}"
    return "x = Error!"


a = int(input("a = "))
b = int(input("b = "))

print(message(a, b))