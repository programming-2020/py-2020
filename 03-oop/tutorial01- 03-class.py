

class Point():
    """
    class point with x and y properties
    """

    def __init__(self, name, x, y):
        """
        __init__ (initialisation method) is a magic method
        """
        self.name = name
        self.x = x
        self.y = y

    def show(self):
        """
            Shows point properties -> name(x, y) 
        """
        return f"{self.name}({self.x}, {self.y})"


a = Point("A", 4, 5)
print(a.show())

b = Point("B", 4, 5)
print(b.show())

# print(a == b) # False
