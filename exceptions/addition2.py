while True:
    try:
        num1 = int(input("Enter number 1: \n>"))
        num2 = int(input("Enter number 2: \n>"))
    except ValueError:
        print("Enter valid number")
        continue
    else:
        result = num1 + num2
        print("SUM: " + str(result))
