prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program. \n>"

#we have initial the variable used in while loopa
message = ""

while message != 'quit':
    message = input(prompt)
    print(message)
