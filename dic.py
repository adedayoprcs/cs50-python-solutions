#HOw to add a key:value to an already existing dictionary
user_profile = {"Name":"Adigun", "Age":35, "Sex":"M",} 
user_profile["Occupation"] = "Doctor"
user_profile["Relationship Status"] = "Single"
(user_profile)

#Modifying an item in a dictionary also takes the same method
user_profile["Age"] = 45
(user_profile)

#examples using alien
Avatar ={"Speed":"Hard", "Gun":"Sniper", "Speed increament":1}
for speed_level in Avatar:
    if Avatar["Speed"] == "Easy":
        Speed_increament = 2
      
        
    elif Avatar["Speed"] == "Medium":
        Speed_increament = 3
       
    else:
        Avatar["Speed"] == "Hard"
        Speed_increament = 5
       

New_Speed =Avatar["Speed increament"] =Avatar["Speed increament"] + Speed_increament
(New_Speed)
#The del is used to delete a key-value from a dictionary permanatly.
del Avatar["Gun"]
(Avatar)
#using the get method to retrive key value from a dictionary
#The get method is used to avoid Keyerror,when we type an item that is not in a dictionary. 
get_avatar = Avatar.get("Gun","Item not in dic")

#How to loop over a dictionary
#Names and their favourite programming Language
favourite_language = {"Pleasant":"Javecritp", "John":"C++", "Precious":"Python", "James":"C"}
names = ["Precious", "John", "James"]
for name, language in favourite_language.items():
    if name in names:
        (name[:])
        (favourite_language[name])
#using the .key() method to loop over each keys in a dictionary. 
for name in favourite_language.keys():
    if name in names:
        languages = favourite_language[name]
        (f"{name}"":"f"{languages}")
   
#Nesting..
alien_0 = {"name":"stranger", "color":"green", "Point":"5"}
alien_1 = {"name":"james", "color":"red", "Point":"5"}
alien_2 = {"name":"johnwick", "color":"white", "Point":"5"}\

aleins = [alien_0, alien_1, alien_2]
for alein in aleins:
   
    aliens_list = []

#Here we write a for loop to do the opration below the for loop.
# we assign a variable alien_number in the for for loop because it's needed to run the loop not because we need it
# we used to following opration to create  alien_0 5 times and save it into a dic. 

for alien_number in range(5):
    alien_0 = {"name":"stranger", "color":"green", "Point":"5"}
    aliens_list.append(alien_0)
    

#Here we run a for loop on the list we had created. 
#each alien is assign to alien_dic
# the an if statement is used to check if the color of that alien assigned to alien dic 
#at the perticular time is green, if Yes, then then a new value is assigned to the color which is blue. 

for alien_dic in aliens_list[:2]:
    if alien_dic["color"] == "green" :
        alien_dic["color"] = "blue"

#Nesting a list into a dic
favourite_language = {"Pleasant":["Javecritp"], "John":["C++", "Python",], "Precious":["Python"], "James":["C", "goland"]}
for name, languages in favourite_language.items():
    
    for language in languages:
        (language)


       






