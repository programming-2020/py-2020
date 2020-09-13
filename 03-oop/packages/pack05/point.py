
from math import sqrt


class Point:
    '''Coordinate system point object\n
    Point has name (string), x (integer), y (integer)'''

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def reposition(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def printPoint(self):
        return f"Point {self.name} ({self.x}, {self.y})"
