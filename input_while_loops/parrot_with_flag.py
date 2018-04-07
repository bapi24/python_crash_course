prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program. \n>"

#initialize a flag
active = True

#use flag instead of a variable
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
