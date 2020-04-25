one = 1
two = 2
three = 3
four = 4

def which_quadrant(n):
    if(n == one):
        return f'x and y are positive'
    elif(n == two):
        return f'x is negative, y is positive'
    elif(n == three):
        return f'x and y are negative'
    elif(n == four):
        return f'x is positive, y is negative'
    else:
        return f'Quadrant does not exist!'


def which_quadrant_message(n):
    return f'Values: {which_quadrant(n)}'


n = int(input('Enter the quadrant: '))

print(which_quadrant_message(n))