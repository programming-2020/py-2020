print("Start")
print("----")
print("Unesi stranice:")

a = float (input ("a = "))
b = float (input ("b = "))
c = float (input ("c = "))
d = float (input ("d = "))

uslov = ((a < c) and (b < d) or (a < d) and (b < c))

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