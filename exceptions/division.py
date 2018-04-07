print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("Enter first number: \n>")
    if first_number == 'q':
        break
    second_number = input("Enter second number: \n>")
    if second_number == 'q':
        break
    # answer = int(first_number)/ int(second_number)
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero!!")
    else:
        print("Result:" + str(answer))
    cont = input("Do you wish to continue?? (y or n) \n>")
    if cont == 'y':
        continue
    elif cont == 'n':
        break
    else:
        print("Give Valid input!!")
