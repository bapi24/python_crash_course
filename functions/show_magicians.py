def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for magician in magicians:
        # g_mag = "The great, " + magician
        magicians.append("The great, " + magician)
    return magicians

#FIXME memory error
magicians = ['troy', 'benny', 'carol']
new_mags = make_great(magicians[:])
show_magicians(magicians)
print(new_mags)
