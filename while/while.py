#The while Loop keeps running as long as a condition remains True.
number = 1
while number <=5:
    (number)
#Here we keep adding one on each osscilation of the while loop
    number +=1

# A program that runs until a user enter quit. 
message = ""
while message != "quit":
    message = input("")
    (message)

#In situation where there are diffrent ways to quit a while loop, we can use a variable as the condition to run the 
#whiile loop. while this condition remains True, the program continues to run till it is false. 
# This is known as flag. 
# The flag is used in complicated codes like games where there diffrent ways the game can stop being in
# an active mode. 
# Active mode = True. once the program is no more in an active mode, we can say the active mode is false.


active = True
while active:
    userinput = input(": ")
    if userinput == "quit":
        active = False
    else:
        (userinput)

# break can also be used with a for loop
# using continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# We also use while loop with a list or a dictionary. 
unverified_users = ["Judge", "Mattew", "Prescillia", "Adra"]
verified_users = []
# This loops runs as long as thier is a value in the unverified users. 
while unverified_users:
    verified_user = unverified_users.pop()
    verified_users.append(verified_user)

for verified_user in verified_users:
    print(verified_user)

#Also, in situation in which we want to remove all instance of a perticular value from a list
pets = ["dog", "cat", "lion", "cat", "goat", "cat"]
while "cat" in pets:
    pets.remove("cat")
print(pets)



