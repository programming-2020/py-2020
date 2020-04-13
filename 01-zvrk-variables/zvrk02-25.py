print("Start")
print("----")
print("Unesi koordinate za Tacku A:")

x1 = float (input ("x1 = "))
y1 = float (input ("y1 = "))

print("Unesi koordinate za Tacku B:")

x2 = float (input ("x2 = "))
y2 = float (input ("y2 = "))

print("Unesi koordinate za Tacku C:")
x3 = float (input ("x3 = "))
y3 = float (input ("y3 = "))

output = ((y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1))

if output == True:
  message = f"Da li tacke pripadaju pravoj: Da!"
  print(message)
else:
  message = f"Da li tacke pripadaju pravoj: Ne!"
  print(message)
print ("----")

