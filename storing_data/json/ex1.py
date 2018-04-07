import json

filename = 'username.json'
data = "Hola!"
data += " amigo"
with open(filename, 'w') as f:
    username = json.dump(data, f)
    # print("Welcome back, " + username + "!")

#reading from json
with open(filename) as f:
    greeting = json.load(f)

print(greeting)
