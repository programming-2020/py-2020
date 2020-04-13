print("Start")
print("----")
print("Unesi koordinate za Tacku A:")

x1 = float (input ("x1 = "))
y1 = float (input ("y1 = "))

print("Unesi koordinate za Tacku B:")

x2 = float (input ("x2 = "))
y2 = float (input ("y2 = "))

kvadrant = ((x1 * x2 > 0) and (y1 * y2 > 0))

if kvadrant == True:
  message = f"Da li se tacke nalaze u istom kvadrantu: Da!"
  print(message)
else:
  message = f"Da li se tacke nalaze u istom kvadrantu: Ne!"
  print(message)
print ("----")