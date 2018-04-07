micky = {
    'type': 'dog',
    'owner': 'henry',
}

jiju = {
    'type': 'snake',
    'owner': 'david',
}

parker = {
    'type': 'dog',
    'owner': 'eshwar',
}

pets = [micky, jiju, parker]

for pet in pets:
    new_pets = sorted(pets, key=len)
    print(pet)
print(new_pets)
