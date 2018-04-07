# #store info about pizza
# pizza = {
#     'crust' : 'thick',
#     'toppings' : ['mushrooms', 'extra cheese'],
# }

pizza = {}
pizza['crust'] = input("Choose from \n a)thin  b)thick ")
print("Enter Toppings:")
topping_list = []
while True:
    topping = input()
    if topping:
        topping_list.append(topping)
    else:
        break
# for x in input().split():
#     topping_list.append(x)

pizza['toppings'] = topping_list

#summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
