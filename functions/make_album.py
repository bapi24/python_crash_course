def make_album(artist_name, album_name, tracks=''):
    '''print dictionary of information about artist'''
    if tracks:
        info = {'artist': artist_name, 'album': album_name, 'tracks': tracks}
    else:
        info = {'artist': artist_name, 'album': album_name}
    print(info)

while True:
    print("#######Enter the details#######")
    ar_name = input("Enter the name of artist: \n> ")
    if ar_name == 'q':
        break
    al_name = input("Enter the album name: \n> ")
    if al_name == 'q':
        break
    make_album(ar_name, al_name)
    
# make_album('satish', 'zilzil')
# make_album('khan', 'mustafi')
# make_album('gayatri', 'saburi')
# make_album('amisha', 'rangoon', 22)
# #
# def make_album(artist_name, album_name, tracks=''):
#     """Return a dictionary of information about an artist."""
#     artist = {'artist': artist_name, 'album': album_name}
#     if tracks:
#         artist['tracks'] = tracks
#     return artist
# artist1 = make_album('jimi', 'hendrix', 27)
# artist2 = make_album('kendrick', 'chillar_max')
# # print(type0(artist1['tracks']))
# print(artist1)
# print(artist2)
