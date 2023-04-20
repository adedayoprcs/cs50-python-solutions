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


