#Nesting Dictionaries into a Dictionary.
# The first for loop is called, then the variable assinged to the value of the dictionary, is used to index the 
# the nested dictionary. 

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton'}, 

'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris'
}}

for user_name, user_info in users.items():
    print(user_info["first"])

 fruits = { "apple" : 130, "avocado" : 50, "banana" : 110, "cantaloupe" : 50,
    "grapefruit":60, "grapes":90, "honeydew melon":50, "kiwifruit":90,
    "lemon":15, "lime":20, "nectarine":60, "orange":80, "peach": 60,
    "pineapple": 0, "plums":70, "strawberries":50, "sweet cherries":100,
    "tangerine":50, "watermelon":80, "pear":100 }

