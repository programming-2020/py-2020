print("Start")
print("----")
print("Unesi polje prve figure")
k = int (input ("Kolona = "))
l = int (input ("Red = "))

print("Unesi polje druge figure")
m = int (input ("Kolona = "))
n = int (input ("Red = "))

#belo_polje = (k + l) % 2 == 0 and (m + n) % 2 == 0
#crno_polje = not belo_polje

prva_figura = k + l
druga_figura = m + n


if (prva_figura % 2 == 0 and druga_figura % 2 == 0) or (prva_figura == druga_figura):
  message = f"Figure su na polju iste boje"
  print(message)
else:
  message = f"Figure nisu na polju iste boje"
  print(message)

print ("----")