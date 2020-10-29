'''
Invalid number exception
'''


class NegativeNumberError (Exception):
    pass


class InvalidNumberException (Exception):
    '''
    Invalid number exception class
    '''

    __zero = 0

    def __init__(self, number):
        try:
            if not isinstance(number, int):
                raise TypeError
            if number <= self.__zero:
                raise NegativeNumberError
            super().__init__("")
            self.__number = number
        except TypeError:
            return f"Invalid input type. Input must be an integer"
        except NegativeNumberError:
            return f"Input must be a positive integer"
