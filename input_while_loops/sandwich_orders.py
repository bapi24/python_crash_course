sandwiches = ['mediterrean', 'super-veg', 'chicken', 'lamb', 'pastrami', 'black bean', 'pastrami', 'pastrami']

print("The Deli has run out of pastrami sandwiches!!")

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

finished_sandwiches = []

while sandwiches:
    sandwich = sandwiches.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print(" \n All sandwich orders have been made")
# print(sandwiches)
# print(finished_sandwiches)
