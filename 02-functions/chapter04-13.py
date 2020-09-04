# TODO:
zero = 0
one = 1


def factorial(n):
    product = 1
    for i in range(one, n):
        product *= i
    return product


def sum_fact(n):
    sum = zero
    for i in range(one, n + one):
    	sum += factorial(i)
    return sum

value = int(input('n = '))
result = sum_fact(value)
message = f'Sum of factorials {result}'
print(message)
