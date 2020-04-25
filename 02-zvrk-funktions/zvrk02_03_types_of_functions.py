def get_greeting(name):
    return f"Hi {name}!"

message = get_greeting("Zvrki")
print(message)

file = open("content.txt", "w")
file.write(message)