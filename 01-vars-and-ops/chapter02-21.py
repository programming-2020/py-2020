
# Convert the given price into bank notes (50, 20, 10, 5, 2, 1)

fifty = 50
twenty = 20
ten = 10
five = 5
two = 2
one = 1

price = int(input("price = "))

fifty_note = price // fifty 
twenty_note = (price % fifty ) // twenty
ten_note = ((price % fifty) % twenty) // ten
five_note = (((price % fifty) % twenty) % ten) // five
two_note = ((((price % fifty) % twenty) % ten) % five) // two
one_note = ((((price % fifty) % twenty) % ten) % five) % two 

message = f'Price {price} = {fifty_note} {twenty_note} {ten_note} {five_note} {two_note} {one_note}'

print(message)

