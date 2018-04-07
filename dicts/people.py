person1 = {
    'name': 'rock',
    'profession': 'actor',
    'age': 45,
}

person2 = {
    'name': 'steph',
    'profession': 'athlete',
    'age': 31,
}

persons = [person1, person2]

for person in persons:
    for k,v in person.items():
        print(k+": "+str(v))
        # print(v)
    print("\n")
