fav_places = {

'alen': ['LA', 'delhi', 'chicago'],
'draymond': ['sacremento', 'san jose', 'phoenix'],
'trey': ['denver', 'dallas', 'philly']

}

for person, places in fav_places.items():
    print("\n" + person + "'s favorite places are:")
    for place in places:
        print("\t"+place)
