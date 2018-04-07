active = True
while active:
    print("Lets add two numbers!!")
    num1 = input("Enter number 1: \n>")
    num2 = input("Enter number 2: \n>")

    try:
        sum = int(num1) + int(num2)
        print("\nResult: " + str(sum))
    except ValueError:
        print("Enter valid numbers!!")
    while True:
        cont = input("Do you want to continue?? ( y or n) \n>")
        if cont == 'n':
            active = False
            break
        elif cont == 'y':
            break
        else:
            print("Enter valid option")
            continue
