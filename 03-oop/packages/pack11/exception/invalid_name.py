'''
Invalid name exception
'''


class InvalidNameException (Exception):
    '''
    Invalid name exception class
    '''

    def __init__(self, name):
        super().__init__("The name cannot be empty")
        self.name = name
