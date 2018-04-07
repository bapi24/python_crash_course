#reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
        # print(line.rstrip()) #to remove places between lines

        
