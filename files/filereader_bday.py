file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: \n>")
if birthday in pi_string:
    print('hooray!!! your birthday appears in pi! ')
else:
    print("your birthday does not appear in pi, better luck next life!!")
