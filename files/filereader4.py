filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


# print(lines) ['3.14\n', '8976\n'....]

pi_string = ''


for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
