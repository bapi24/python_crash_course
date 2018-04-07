active = True
filename = 'guest2.txt'

while active:
    name = input("Hola!! Como te llamas\n>").title()
    if name == 'Quit' or 'quit':
        active = False
    else:
        with open(filename, 'a') as f_obj:
            f_obj.write(name.title() + "\n")
        greeting = "Beinvenido " + name + "!!, usted ha sido agregado"
        greeting += " al libro de visitas"
        print(greeting)
        continue
