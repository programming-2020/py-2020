
from box import Box


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
