
user_profile = {"Name":"Adigun", "Age":35, "Sex":"M",}
get_key = user_profile["Name"]
print(get_key)
# To get the value of a key.
#How old is Adigun? 
for value in user_profile:
    if value["Age"] == 35:
        print(user_profile["Age"])

    


item_price = {}
while True:
    try:
        item = input ("Item: ").title()
        for item_, price in items.item():
            if item in items:
                try:
                    item_price.update({item:items[item]})
                    item_sum = sum(item_price.values())
                    print(f"${round(item_sum,2)}")
                except KeyError:
                    pass
    except EOFError:
            print("\n")
            break
 