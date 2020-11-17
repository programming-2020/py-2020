'''
Exception handling
Exception is an object inherited fro mbuilt-in class BaseException
'''


def isEven(number):
    if not isinstance(number, int):
        raise TypeError(f"Number {number} is not an integer")
    if number % 2:
        raise ValueError(f"Number {number} is not even")
    return f"Number {number} is an even number"


# print(isEven(3))
# print(isEven("3"))
three = 3
zero = 0


def isDevisibleByThree(number):
    try:
        if number == zero:
            raise ZeroDivisionError
        if not isinstance(number, int):
            raise TypeError
        if number % three != zero:
            raise ValueError
        return f"Number can be devided by three"
    except ZeroDivisionError:
        return "Cannot devide by zero"
    except TypeError:
        return f"The inserted value must be an integer"
    except ValueError:
        return f"The value cannot be divided by three"


print(isDevisibleByThree(9))
print(isDevisibleByThree(0))
print(isDevisibleByThree(8))
print(isDevisibleByThree("33"))
