
from math import sqrt


class Point:
    '''Coordinate system point object\n
    Point has name (string), x (integer), y (integer)'''

    def __init__(self, name, x, y):
        '''Initaialize (initialise) a Point object '''
        self.name = name
        self.x = x
        self.y = y

    def reposition(self, x, y):
        '''Change the position of the current point instance'''
        self.x = x
        self.y = y

    def distance(self):
        '''Calculated the distance from O(0, 0)'''
        return sqrt(self.x ** 2 + self.y ** 2)

    def printPoint(self):
        '''Print the point properties'''
        return f"Point {self.name} ({self.x}, {self.y})"
