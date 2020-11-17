

class Person(object):
    """
    Person: name and email
    """

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @name.setter
    def setName(self, name):
        self.__name = name

    @email.setter
    def setEmail(self, email):
        self.__email = email

    @name.deleter
    def deleteName(self):
        del self.__name

    @email.deleter
    def deleteEmail(self):
        del self.__email


first = Person('John', 'john@mail.com')
print(first.name)
print(first.email)
first.setName = "Adam"
print(first.name)
print(first.email)
