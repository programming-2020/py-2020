from packages.pack05.point import Point

# help(Point)

a = Point("A", 4, 5)
print(a.printPoint())
print(f"Distance from 0 = {a.distance()}")

a.reposition(3, 4)
print(a.printPoint())
print(f"Distance from 0 = {a.distance()}")
