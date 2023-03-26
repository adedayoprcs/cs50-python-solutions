# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
for alien_number in range(30):
    
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

print({len(alien)})