prompt = "\n What is your age? \n>"
age = ""

while age != 'quit':
    # age = int(input("What is your age?"))
    age = input(prompt)
    if age != 'quit':
        if int(age) < 3:
            ticket_price = 3

        elif int(age) >= 3 and int(age) < 12:
            ticket_price = 10

        else:
            ticket_price = 15

        print("The price of your ticket is: " + str(ticket_price))
