responses = {}

#set a flag
polling_active = True

while polling_active:
    #prompt for the person's name and response.
    name = input("\nWhat is your name? \n> ")
    response = input("Which mountain would you like to climb someday? \n> ")
    #store the response in the dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) \n> ")

    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n --- Poll Results ----")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
