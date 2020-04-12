print("Start")
print("----")
print("Unesi odsecke:")

x = float (input ("x = "))
y = float (input ("y = "))
z = float (input ("z = "))

uslov = (x + y > z) and (x + z > y) and (y + z > y)

p = uslov
message = f"p je: = {p}"
print(message)


if p == True:
  message = f"Uslov je ispunjen"
  print(message)
else:
  message = f"Uslov nije ispunjen"
  print(message)
print ("----")
