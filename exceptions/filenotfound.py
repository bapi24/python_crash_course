filename = 'alice.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, there is no file with the name " + "'" + filename + "'"
    print(msg)

else:
    words = contents.split()
    num_words = len(words)
    # print(type(words))
    print(("The file ") + filename + " has about " + str(num_words) + " words.")
