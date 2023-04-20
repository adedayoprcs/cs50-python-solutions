# Problem
# 1. Prompts the user for a level an iteger between 1-3, (done)
# If the user does not input 1, 2, or 3, the program should prompt again. (done)
# 2. using the user's input, generate 10 math problmes that only supports the addition opration. (+)
# 3. Prompts the user to solve each of those problems.
# If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
# allowing the user up to three tries in total for that problem. If the user has still not answered
# correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.

# My Solution
import random


def main():
    
    correct_answers = []
    user_input = get_level()
    for i in range(10):
        if int(user_input) == 1:
            x = random.randrange(0 , 9)
            y = random.randrange(0, 9)
        elif int(user_input) == 2:
            x = random.randrange(10 , 99)
            y = random.randrange(10, 99)
        else:
            x = random.randrange(100 , 999)
            y = random.randrange(100, 999)

        sum_of_equation = int(x) + int(y)
        print(f"{x}" " " "+" " " f"{y}" " ""=", end=" ")
        user_ans = input("")
        if generate_integer(user_ans) and int(user_ans) == sum_of_equation:
            correct_answers.append(int(user_ans))
            continue
        else:
            for j in range(2):
                print("EEE")
                print(f"{x}" " " "+" " " f"{y}" " ""=", end=" ")
                user_ans = input("")
                if generate_integer(user_ans) and int(user_ans) == sum_of_equation:
                    correct_answers.append(int(user_ans))
                    break
            else: 
                print("EEE")
                print(f"{x}" " " "+" " " f"{y}" " ""="" " f"{sum_of_equation}")
    else:
        score = sum(correct_answers)
        print("Score: " f"{score}")
    

                

         
                
                   
            



    











def generate_integer(level):
    """This function takes an input and check if the user input is an integer"""
    while True:
        try:
            num = int(level)
            if int(num) < 1 :
                return False
        except ValueError:
            return False
        else:
            return True



def get_level():
    while True:
        level = (input("level: "))
        if generate_integer(level):
            if int(level) >= 1 and int(level) <= 3:
                return int(level)






if __name__ == "__main__":
    main()















































