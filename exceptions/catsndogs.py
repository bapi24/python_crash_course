def display(filename):
    try:
        with open(filename) as f:
            content = f.read()
            f.close()
    except FileNotFoundError:
        # print("File " + filename + " is not present\n")
        pass
    else:
        print("Contents of the file " + filename + ":  \n######################\n" + content)

file_name = ['dogs.txt', 'fds.txt', 'cats.txt', 'dfs.txt']

for file in file_name:
    display(file)
