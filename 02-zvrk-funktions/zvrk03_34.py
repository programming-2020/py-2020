one = 1
two = 2
three = 3
four = 4
five = 5

def grade(n):
    if(n == one):
        return f'nedovoljan'
    elif(n == two):
        return f'dovoljan'
    elif(n == three):
        return f'dobar'
    elif(n == four):
        return f'vrlo dobar'
    elif(n == five):
        return f'odlican'
    else:
        return f'Niste uneli odgovarajucu ocenu!'


def grade_message(n):
    return f'Ocena je: {grade(n)}'


n = int(input('Unesite ocenu: '))

print(grade_message(n))