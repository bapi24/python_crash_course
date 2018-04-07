filename = 'guestbook.txt'
active = True

print("Enter 'q' when you are finished!")

while active:
    name = input("Hola! Como te llamas?\n>")
    if name == 'q':
        active = False
        break
    else:
        with open(filename, 'a') as f:
            f.write(name.title()+"\n")
        print("Hi " + name+ "! Your name has been added to the guestbook!")
