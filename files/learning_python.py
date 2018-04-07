file_name = "learning_python.txt"

print("----Reading Entire File----")
with open(file_name) as f_obj:
    contents = f_obj.read()
    print(contents)

print("----looping over the lines----")
with open(file_name) as f_obj:
    for line in f_obj:
        print(line.rstrip())

print("---storing lines in list----")
with open(file_name) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.rstrip())
