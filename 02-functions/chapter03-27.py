# given three-figure number a
# check if it is narcissistic number (Armstrong number)
# Armstrong number is a number that is equal
# to the sum of cubes of its digits. 153, 370, 371 and 407
# 153 = 1*1*1+5*5*5+3*3*3

zero = 0
ten = 10
hundred = 100
thousand = 1000


def positive(n):
    return n > zero


def three_figure(n):
    return hundred <= n < thousand
    # return (zero <= (n / hundred) < ten)
    # return ((n / hundred) >= zero) and ((n / hundred) < ten)


def armstrong(n):
    if positive(n) and three_figure(n):
        a = n // hundred  # 153 / 100 = 1
        b = (n % hundred) // ten  # 153 % 100 = 53 # 53 / 10 = 5
        c = (n % hundred) % ten  # 153 % 100 = 53 # 53 % 10 = 3
        return a ** 3 + b ** 3 + c ** 3 == n
    return zero


def message(n):
    if armstrong(n):
        return f'n = {n} is Armstrong'
    elif not three_figure(n):
        return f'n = {n} is invalid'
    else:
        return f'n = {n} is not Armstrong'


a = int(input("a = "))

print(message(a))
