prompt = "\n What is your age? \n>"

active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False
        break
    else:
        try:
            age = int(age)
            if age < 3:
                ticket_price = 3

            elif age >= 3 and age < 12:
                ticket_price = 10

            elif age < 101:
                ticket_price = 15
            else:
                print("Woahhh! are you sure?\n")
                continue
            print("The price of your ticket is: " + str(ticket_price))
        except ValueError:
            #Handle the exception
            print("Please enter valid number!")
