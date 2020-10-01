# Diamond problem solved

class BaseClass(object):
    """
    Base class for illustrating the diamond problem
    """
    instance = 0

    def __init__(self):
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

    def __init__(self):
        """
        class instatiation number
        """
        super().__init__()
        LeftClass.instance += 1
        print(f"LeftClass = {LeftClass.instance}")


class RightClass(BaseClass):
    """
    Right class iherits the Base class for illustrating
    the diamond problem
    """
    instance = 0

    def __init__(self):
        """
        class instatiation number
        """
        super().__init__()
        RightClass.instance += 1
        print(f"RightClass = {RightClass.instance}")


class SubClass(LeftClass, RightClass):
    """
    Subclass inherits the Left class and Right class
    for illustration of the diamond problem
    """
    instance = 0

    def __init__(self):
        """
        class instatiation number
        """
        super().__init__()
        SubClass.instance += 1
        print(f"SubClassBad = {SubClass.instance}")
