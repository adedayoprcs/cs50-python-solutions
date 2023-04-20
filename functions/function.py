
# it is possible to use the agument with = to declear the value of the agument just to be
# more clear. we can also just input this arguments in positions. specified from the functions
# this is known has "KEYWORD ARGUMENT" without using the equals to is a "POSITIONAL ARGUMENT"
def main():
        describe_pet(petname= "Bingo")
# """ """ three quotes is used to describe what the function does. 
# This is important whenever we create a function. 
def greet_user(username ="Jon doe"):
        """Says Hello to user"""
        print("Hello"" "f"{username}")


# We can assign a default value to a function if it's called an no argument is assinged to 
# it. 
# Assigning a defaul value to argument can also be used to avoid argument error. 

def describe_pet(petname = "wille", pet_type = "Dog"):
        """Describe pet"""
        petname = petname.strip()
        print(f"{petname}"" ""is a very good" " "f"{pet_type}")

main()
    
