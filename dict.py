
user_profile = {"Name":"Adigun", "Age":35, "Sex":"M",}
get_key = user_profile["Name"]
print(get_key)
# To get the value of a key.
#How old is Adigun? 
for value in user_profile:
    if value["Age"] == 35:
        print(user_profile["Age"])

    