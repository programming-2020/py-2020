# '''Inheritance example with overriding'''

from packages.pack07.parcel import Parcel

help(Parcel)
a = Parcel("First parcel", 5, 4, 3, 700, "Cardbord")
print(a.show())
