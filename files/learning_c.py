file_name = "learning_python.txt"

with open(file_name) as f_obj:
    for line in f_obj:
        line.replace('Python', 'C')
        print(line.rstrip().replace('Python', 'C'))
