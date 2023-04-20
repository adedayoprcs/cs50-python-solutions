# First approach
responses = {}
while True:
    name = input("\n: ")
    response = input (": ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        break

print(responses)

#Second approach

Loop_acitve = True

while Loop_acitve:
    name = input("\n: ")
    response = input (": ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        Loop_acitve = False
print(responses)