zero = 0
one = 1
ten = 10
hundred = 100


def armstrong(m):
    i = zero
    for i in range (i , m + one):
        a = m // hundred 
        b = (m % hundred) // ten 
        c = (m % hundred) % ten 
        if a ** 3 + b ** 3 + c ** 3 == m:
            return f'{m} is Armstrong'
        else:
            return f'{m} is not Armstrong'
    

m = int(input("m = "))

message = f'{armstrong(m)}'
print(message)