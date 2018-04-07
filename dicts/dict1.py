person1 = {

    'first_name' : 'tarun',
    'last_name' : 'gog',
    'age' : 28,
    'city' : "vij"

}

# def print_name(person):

print("\nDetails:")
print("The first name:" + person1['first_name'])
print("The last name:" + person1['last_name'])
print("The age:" + str(person1['age']))
print("The city:" + person1['city'])

print("\n\n")

# store fav numbers
players = {

    'kobe' : 24,
    'jordan' : 23,
    'dirk' : 41,
    'messi' : 10,
    'iniesta' : 12
}

for key, value in players.items():
    print(key+"'s fav number: " + str(value))

print(players.keys())
print("\n \n")

#rivers and countries
rivers = {
    'nile' : 'egypt',
    'ganga' : 'india',
    'amazon' : 'brazil'
}

#print keys and values
for k, v in rivers.items():
    print("The " +k + " runs through "  + v + ".")

#print keys
for k in rivers:
    print(k)

#print values
for v in rivers.values():
    print(v)
