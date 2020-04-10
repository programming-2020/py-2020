from math import sqrt

print ("Start")
print ("----")

print("Tacka (Koordinata x, Koordinata y)")
tx = float(input("tx = "))
ty = float(input("ty = "))

x = 1
y = 0

poluprecnik = sqrt(x**2 + y**2)
poluprecnik_tacke = sqrt((x - tx)**2 + (y - ty)**2)

output = poluprecnik <= poluprecnik_tacke

message = f"Output = {output}"
print(message)
print("----")