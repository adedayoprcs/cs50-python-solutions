# Make an empty list for storing aliens.
aliens = []

# Make new 30 green aliens.
new_alien = {'color' : {"red": "00", "blue:": "01"}, 'points': 5, 'speed': 'slow'}
new_variable = new_alien["color"]["red"]
print(new_variable)


for alien_number in range(30):
    new_alien["color"] = "green"
    aliens.append(new_alien)
    
    

# Show the first 5 aliens.
for alien in aliens[:5]:
    new_alien['color'] = "yellow"
    new_alien["points"] = "10"
    

