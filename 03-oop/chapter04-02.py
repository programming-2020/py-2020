'''
Properties - another simple example
'''


class Contact(object):
    """
    Properties - another simple example
    """

    def __init__(self, fullname, email):
        self.__fullname = fullname
        self.__email = email

    def __getFullname(self):
        return self.__fullname

    def __setFullname(self, fullname):
        self.__fullname = fullname

    def __delFullname(self):
        del self.__fullname

    def __getEmail(self):
        return self.__email

    def __setEmail(self, email):
        self.__email = email

    def __delEmail(self):
        del self.__email

    fullname = property(__getFullname, __setFullname,
                        __delFullname, "Contact's fullname properties")

    email = property(__getEmail, __setEmail, __delEmail,
                     "Contact's email properties")


a = Contact("John", "john@mail.com")
b = Contact("Jane", "jane@mail.com")

print(b.fullname)
b.email = "jbc@mail.com"
print(b.email)
del b.email
# print(b.email) # AttributeError: 'Contact' object has no attribute '_Contact__email'
b.email = "new@mail.com"
print(b.email)
