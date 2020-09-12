from math import sqrt


class Point:
    '''Coordinate system point'''

    def __init__(self, name, x, y):
        '''Point object initalization'''
        super().__init__()
        self.name = name
        self.x = x
        self.y = y

    def reposition(self, x, y):
        '''Change the point's coordinates'''
        self.x = x
        self.y = y

    def distance(self):
        '''Calculates the distance from the beginning of\
        coordinate system'''
        return sqrt(self.x ** 2 + self.y ** 2)

    def showProperties(self):
        return f"({self.x}, {self.y})"
