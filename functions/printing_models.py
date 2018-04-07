'''

Consider a company that creates 3D printed models of designs
that users submit. Designs that need to be printed are stored
in a list, and after being printed they’re moved to a separate
list. The following code does this without using functions:

unprinted_designs = ['iphone case', 'motivational poster', 'copper jug']
printed_designs = []

#simulate printing designs until none left
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #simulate creating a 3D print from the design
    print("Printing model: " + current_design)
    printed_designs.append(current_design)


#display all completed models.
print("\nThe following models have been printed:")

for printed_design in printed_designs:
    print(printed_design)
'''

#above program using funcitons
def print_models(unprinted_designs, printed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing Model: " + current_design)
        printed_designs.append(current_design)

def show_completed_models(printed_designs):
    print("\nThe following models have been printed: ")
    for printed_design in printed_designs:
        print(printed_design)


unprinted_designs = ["ferrero rocher", "fifa 19", "lollipop"]
printed_designs = []
print_models(unprinted_designs, printed_designs)
show_completed_models(printed_designs)
