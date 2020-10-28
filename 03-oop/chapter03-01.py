
'''
Properties simple example
'''


class Contact:

    def __init__(self, fullname, email):
        self.__fullname = fullname
        self.__email = email

    def _setName(self, fullname):
        if not fullname:
            raise Exception("The name is invalid")
        self.__fullname = fullname

    def _getName(self):
        return self.__fullname

    fullname = property(getName, setName)


a = Contact("ABCD", "abc@mail.com")
print(a.fullname)
a.fullname = "New One"
print(a.fullname)
a.fullname = ""
