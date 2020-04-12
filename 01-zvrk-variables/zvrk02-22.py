print("Start")
print("----")
print("Unesi vremenski period:")

sat1 = int (input ("Sat na pocetku = "))
min1 = int (input ("Minut na pocetku = "))
sat2 = int (input ("Sat na kraju = "))
min2 = int (input ("Minut na kraju = "))

razlika = sat2 * 60 + min2 - (sat1 * 60 + min1)
sat_ukupno = razlika // 60
min_ukupno = razlika % 60

message = f"Ukupno vreme je: = {sat_ukupno} sata i {min_ukupno} minuta"
print(message)
print("----")