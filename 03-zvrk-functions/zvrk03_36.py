one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7

def day_of_the_week(n):
    if(n == one):
        return f'ponedeljak'
    elif(n == two):
        return f'utorak'
    elif(n == three):
        return f'sreda'
    elif(n == four):
        return f'cetvrtak'
    elif(n == five):
        return f'petak'
    elif(n == six):
        return f'subota'
    elif(n == seven):
        return f'nedelja'
    else:
        return f'Niste uneli odgovarajuci broj!'


def day_of_the_week_message(n):
    return f'Dan u nedelji je: {day_of_the_week(n)}'


n = int(input('Unesite broj: '))

print(day_of_the_week_message(n))