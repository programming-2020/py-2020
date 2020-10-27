class Person(object):

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


class Address(object):

    def __init__(self, state, city, street):
        self.state = state
        self.city = city
        self.street = street


class Friend(Person, Address):
    def __init__(self, phone, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
