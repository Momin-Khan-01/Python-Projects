# Rock, Paper, Scissor Game 

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("enter choice = Rock, Paper, Scissor = ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer Choice = {computer_choice}")

if user_choice == computer_choice:
    print("Both choices same = Match Tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashed Scissor = You win")

elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts Paper = Computer Win")
    else:
        print("Paper cover Rock = You Win")

elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissor cuts Paper = You win")
    else:
        print("Rock smashed Scissor = Computer win")