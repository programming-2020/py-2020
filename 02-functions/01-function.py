def message():
    text = "Hello"
    print(text)


def my_message(name):
    text = f'Hello {name}'
    print(text)
    return
    print('New text')


my_message('ABC')


def pi():
    return 3.141529


def area_circle(r):
    return r ** 2 * pi()


def odd(n):
    return n % 2 != 0


print(not odd(432))
