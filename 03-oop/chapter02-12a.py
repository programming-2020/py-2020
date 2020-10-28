'''
Exceptions - Custom made exceptions
'''


class InvalidNameException (Exception):
    def __init__(self, name):
        super().__init__("The name cannot be empty")
        self.name = name


class Contact:
    def __init__(self, name):
        try:
            if not name:
                raise InvalidNameException(name)
            self.name = name
        except InvalidNameException as error:
            return f"Invalid name input -> {error}"


a = Contact("")
print(a.name)
