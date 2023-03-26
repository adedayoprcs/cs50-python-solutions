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
        print(name[:])
        print(favourite_language[name])
#using the .key() method to loop over each keys in a dictionary. 
for name in favourite_language.keys():
    if name in names:
        languages = favourite_language[name]
        print(f"{name}"":"f"{languages}")
   
#Nesting..
alien_0 = {"name":"stranger", "color":"green", "Point":"5"}
alien_1 = {"name":"james", "color":"red", "Point":"5"}
alien_2 = {"name":"johnwick", "color":"white", "Point":"5"}\

aleins = [alien_0, alien_1, alien_2]
for alein in aleins:
    print(alein)




