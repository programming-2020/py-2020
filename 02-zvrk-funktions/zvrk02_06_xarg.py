def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

#print(multiply(2, 3, 4, 5))


def my_numbers(*n):
    for i in n:
        print(i)


my_numbers(1, 2, 3)
my_numbers(1, 2, 3, 4)
my_numbers(2, 4, 6, 8, 10)