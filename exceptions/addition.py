'''
input two values
write a function which adds two numbers
include try except for value errors
'''

def sum(num1,num2):
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("Check input you have entered!!")
    else:
        print("result: " + str(sum))

num1 = input("Enter number1: \n>")
num2 = input("Enter number2: \n>")
while True:
    sum(num1, num2)
