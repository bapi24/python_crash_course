'''
program to search for a word in a given file
open file
split the words and save to a list
search the list
'''

filename = 'word_search2.txt'


def search_word(word):
    count = 0
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist!"
        print(msg)
    else:
        words = contents.split()

        for w in words:
            if w == word:
                count += 1
        # print("total count" + str(count))

        if count > 0:
            print("There was a match!!")
            print("The word appeared " + str(count) + " times!")
        else:
            print("There was no match!!")



sword = input("Enter the word you want to search: \n>")
search_word(sword)
