

class Rectangle:
    '''Quadrilateral with four right angles '''

    def __init__(self, length, width):
        '''Initalise the rectangle by providing length and width values'''
        self.length = length
        self.width = width

    def resize(self, length, width):
        '''Resize the existing rectangle'''
        self.legth = length
        self.width = width

    def area(self):
        '''Area of the rectangle '''
        return self.length * self.width

    def perimeter(self):
        '''Perimeter of the rectangle'''
        return 2 * (self.length + self.width)

    def rectangleStr(self):
        '''String values of the rectangle'''
        return f"length={self.length} width={self.width}"


help(Rectangle)

a = Rectangle(4, 5)
print(a.rectangleStr())
