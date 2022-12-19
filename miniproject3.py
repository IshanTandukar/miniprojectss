import random

user_wins = 0
computer_wins = 0
draw_counts = 0

options = ["rock","paper","scissors"]
options[0]

while True:
    user_input = input("Type Rock / Paper / Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock : 0,paper : 1,scissors : 2
    computer_pick = options[random_number]
    print("Computer picked" , computer_pick +".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1    
       
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Its a draw")
        draw_counts += 1   

    elif user_input == "rock" and computer_pick == "rock":
        print("Its a draw")
        draw_counts += 1    

    elif user_input == "paper" and computer_pick == "paper":
        print("Its a draw")
        draw_counts += 1    
 
    else:
        print("You lost!")
        computer_wins += 1    
 

print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")     
print("It was a draw",draw_counts,"times.")   
if (user_wins < computer_wins):
    print("Loooool you loserrrrr")
elif(user_wins > computer_wins):
    print("Beginner's luck")
else:
    print("Whatever")   

print("Goodbye!")





