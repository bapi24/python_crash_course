import json

filename = 'favnum.json'

with open(filename) as f:
    favnum = json.load(f)

print("I know that your fav num is " + favnum)
