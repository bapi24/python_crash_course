name = input("Hola, Como te llamas?\n>")
filename = 'guest.txt'
with open(filename, 'w') as f_obj:
    f_obj.write(name)
