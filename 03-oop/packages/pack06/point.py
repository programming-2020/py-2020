from math import sqrt


class Point:
    '''Coordinate system point object\nPoint has name (string), x (integer), y (integer)'''

    def __init__(self, name, x, y):
        '''Initaialize (initialise) a Point object '''
        self.__name = name
        self.__x = x
        self.__y = y

    def reposition(self, x, y):
        '''Reposition the point object '''
        self.__x = x
        self.__y = y

    def distance(self):
        '''Calculated the distance from O(0, 0)'''
        return sqrt(self.__x ** 2 + self.__y ** 2)

    def printPoint(self):
        '''Print the point properties'''
        return f"Point {self.__name} ({self.__x}, {self.__y})"
