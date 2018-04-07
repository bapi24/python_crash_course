players = {

    'kbraynt': {
        'first': 'kobe',
        'last': 'braynt',
        'location': 'Los Angeles',
    },

    'Mjordan': {
        'first': 'Michael',
        'last': 'jordan',
        'location': 'chicago',
    },
}

#print player details
for playername, player_info in players.items():
    print("\n Playername:" + playername)
    full_name = player_info['first'] + " " + player_info['last']
    location = player_info['location']

    print("\t Full name: " + full_name.title())
    print("\t Location: " + location.title())
