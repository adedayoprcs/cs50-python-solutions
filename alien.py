# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
for alien_number in range(30):
    new_alien["color"] = "green"
    aliens.append(new_alien)
    print(aliens[:5])
    

# Show the first 5 aliens.
for alien in aliens[:5]:
    new_alien['color'] = "yellow"
    new_alien["points"] = "10"
    print(alien)