
'''
Properties simple example
'''


class Contact:

    def __init__(self, fullname, email):
        self.__fullname = fullname
        self.__email = email

    def __setName(self, fullname):
        if not fullname:
            raise Exception("The name is invalid")
        self.__fullname = fullname

    def __getName(self):
        return self.__fullname

    # Order is important - first get, second set
    fullname = property(__getName, __setName)


a = Contact("ABCD", "abc@mail.com")
print(a.fullname)
a.fullname = "New One"
print(a.fullname)
a.fullname = ""
print(a.fullname)
