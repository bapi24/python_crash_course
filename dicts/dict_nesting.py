#create green aliens

#make empty list
aliens = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#print first 5 aliens
for alien in aliens[:5]:
    print(alien)

print("......\n")

#to show number of aliens created
print("Total number of aliens created: "+str(len(aliens)))
