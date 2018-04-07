filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


# print(lines) ['3.14\n', '8976\n'....]

for line in lines:
    print(line.rstrip())
