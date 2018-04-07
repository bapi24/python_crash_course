import json

filename = 'favnum.json'
favnum = input("What is your fav num? \n>")
with open(filename, 'w') as f:
    json.dump(favnum, f)
