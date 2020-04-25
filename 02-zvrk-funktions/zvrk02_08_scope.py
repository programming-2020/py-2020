message = "a"

def greet(name):
    global message
    message = "b"

greet ("Zvrki")
#print(message)

a = 2

def inc (a):
    print(a)
    a += 2
    print(a)

inc(a)
print(a)