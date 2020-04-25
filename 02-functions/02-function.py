
def odd(n):
    return n % 2 != 0


def odd_message(n):
    if odd(n):
        return f'{n} is odd'
    return f'{n} is even'


###################

a = int(input("a = "))
message = f'Odd = {odd_message(a)}'
print(message)

###########
