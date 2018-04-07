import json
filename = 'favnum.json'

def get_stored_num():
    # filename = 'favnum.json'
    try:
        with open(filename) as f:
            favnum = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favnum

def get_new_num():
    favnum = input("What is your fav num? \n>")
    with open(filename, 'w') as f:
        json.dump(favnum, f)
    return favnum

def print_fav_num():
    favnum = get_stored_num()
    if favnum:
        check = input("Is your fav num " + favnum +" ? [y/n]\n>")
        if check == "y":
            print("hoooyaahhh! got that one right")
        else:
            favnum = get_new_num()
            print("We will remember your fav number " + favnum)
    else:
        favnum = get_new_num()
        print("We will remember your fav number!")

print_fav_num()
