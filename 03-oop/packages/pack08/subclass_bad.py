# Diamond problem

class BaseClass(object):
    """
    Base class for illustrating the diamond problem
    """
    instance = 0

    def callMe(self):
        """
        class instatiation number
        """
        BaseClass.instance += 1
        print(f"BaseClass = {BaseClass.instance}")


class LeftClass(BaseClass):
    """
    Left class inherits the Base class for illustrating
    the diamond problem
    """
    instance = 0

    def callMe(self):
        """
        class instatiation number
        """
        BaseClass.callMe(self)
        LeftClass.instance += 1
        print(f"LeftClass = {LeftClass.instance}")


class RightClass(BaseClass):
    """
    Right class iherits the Base class for illustrating
    the diamond problem
    """
    instance = 0

    def callMe(self):
        """
        class instatiation number
        """
        BaseClass.callMe(self)
        RightClass.instance += 1
        print(f"RightClass = {RightClass.instance}")


class SubClassBad(LeftClass, RightClass):
    """
    Subclass inherits the Left class and Right class
    for illustration of the diamond problem
    """
    instance = 0

    def callMe(self):
        """
        class instatiation number
        """
        LeftClass.callMe(self)
        RightClass.callMe(self)
        SubClassBad.instance += 1
        print(f"SubClassBad = {SubClassBad.instance}")
