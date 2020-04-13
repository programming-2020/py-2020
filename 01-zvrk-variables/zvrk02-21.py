print("Start")
print("----")
print("Unesi cenu artikla:")

cena = int (input ("cena: "))
apoen_500_din = cena // 500
cena = cena % 500  
apoen_100_din = cena // 100
apoen_1_din = cena % 100

message = f"Artikal se moze platiti u apoenima: \n500din: {apoen_500_din} kom \n100din: {apoen_100_din} kom \n1din: {apoen_1_din} kom"
print(message)
print("----")