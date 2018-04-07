import json

def get_fav_num():
    favnum = input("What is your fav number? ")
    return favnum

def print_fav_num(favnum):
    print("Your favourite number is: " + favnum)


favnum = get_fav_num()
print_fav_num(favnum)
