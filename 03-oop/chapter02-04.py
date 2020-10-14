from math import sqrt


class Point:
    '''Coordinate system point'''

    def __init__(self, name, x=0, y=0):
        '''Initalization of the point'''
        self.name = name
        self.x = x
        self.y = y

    def reset(self, x, y):
        '''Reset the point coordinates'''
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def printPoint(self):
        return f"Point {self.name} ({self.x}, {self.y})"


help(Point)

a = Point("A", 4, 5)
print(a.printPoint())
print(f"Distance from 0 = {a.distance()}")

a.reset(3, 4)
print(a.printPoint())
print(f"Distance from 0 = {a.distance()}")
