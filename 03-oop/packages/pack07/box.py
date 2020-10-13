
class Box(object):
    '''Box class'''

    def __init__(self, label, length, width, height):
        self.__label = label
        self.__length = length
        self.__width = width
        self.__height = height

    def volume(self):
        return self.__length * self.__width * self.__height

    def show(self):
        return f"Box: {self.__label} Length: {self.__length} Width: {self.__width} Height: {self.__height}"
