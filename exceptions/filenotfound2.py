filename = 'alice.txt'

try:
    with open(filename) as f:
        contents = f.readlines()
except FileNotFoundError:
    msg = "Sorry, there is no file with the name " + "'" + filename + "'"
    print(msg)

else:
    #count approx number of words in the file
    for line in contents:
        print(line)
        words = line.split(',')
        print(words[-1][0:-2])

#origial
    num_words = len(words)
    # print(type(words))
    print(("The file ") + filename + " has about " + str(num_words) + " words.")
