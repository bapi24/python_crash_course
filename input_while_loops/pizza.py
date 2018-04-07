print("Hola!!! What toppings do you want?")
pizza_toppings = ""
toppings_list = []
while pizza_toppings != 'quit':
    pizza_toppings =input("> ")
    toppings_list.append(pizza_toppings)
    if pizza_toppings != 'quit':
        print("We will add " + pizza_toppings + " on your pizza")


#summary of toppings
print("\nTopping ordered:")
for t in toppings_list:
    print(" >" + t)
