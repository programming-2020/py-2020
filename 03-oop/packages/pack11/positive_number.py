'''
'''
from exception.invalid_number import InvalidNumberException, text

print(text())


class NegativeNumberError (Exception):
    def __init__(self):
        """
        docstring
        """
        super().__init__("Input must be a positive integer")


class PositiveNumber:
    '''
    Positive integer value class
    '''
    __zero = 0

    def __init__(self, number):
        """
        docstring
        """
        self.__number = number
    # def __init__(self, number):
    #     try:
    #         if not isinstance(number, int):
    #             raise TypeError("Invalid input type. Input must be an integer")
    #         if number <= self.__zero:
    #             raise Exception("Input must be a positive integer")
    #         else:
    #             self.__number = number

    def getName(self):
        """
        docstring
        """
        return self.__number

# n = PositiveNumber("sadf")
# print(n.getNumber())
