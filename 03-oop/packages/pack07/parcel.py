
# from box import Box

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


class Parcel(Box):
    '''Parcel class'''

    def __init__(self, label, length, width, height, weight, material):
        '''__init__ override example'''
        super().__init__(label, length, width, height)
        self.__weight = weight
        self.__material = material

    def show(self):
        '''show() override example'''
        return f"{super().show()} Weight: {self.__weight} grams Material: {self.__material}"


# a = Parcel("First parcel", 5, 4, 3, 700, "Cardbord")
# print(a.show())
