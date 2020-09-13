from packages.pack05.point import Point

# help(Point)

a = Point("A", 4, 5)
print(a.printPoint())
print(f"Distance from 0 = {a.distance()}")

# change object property value
a.x = 2
print(a.printPoint())

a.reposition(3, 4)
print(a.printPoint())
print(f"Distance from 0 = {a.distance()}")
