message = "a"

def greet(name):
    global message
    message = "b"

greet ("Zvrki")
print(message)