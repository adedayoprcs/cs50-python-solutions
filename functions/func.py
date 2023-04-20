def get_formatted_name(first_name, last_name):
    full_name = f"{first_name}" " " f"{last_name}"
    return full_name





print("please input your full name")
print("input q when you are ready to quite the program")
while True:
    f_name = input("please enter your first name: ")
    if f_name =="q":
        break

 
    
   
    last_name = input("please enter your last name: ")
    if last_name == "q":
        break
    print(get_formatted_name(f_name, last_name))







