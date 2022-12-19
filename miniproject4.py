name = input("Type your name: ")
print("Welcome",name,"to this adventure")

answer = input( "You are on a dirt road , it has come to an end and you can go 'left' or 'right'.Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk around and 'swim' to swim across: ")

    if answer == "swim":
        print("You swam across at got slaughtered by crocodiles.")
    elif answer == "walk":
        print("You died out of fatigueness.")
    else:
        print("Not a valid option. You lose")        

elif answer == "right":
    answer = input("You have come to a bridge. The break looks in a bad state. Would you like to (cross/walk back)? ")

    if answer == "cross":
        print("Well , it was hard but you managed it. Now you meet a stranger .")
        answer = input("Do you talk to them (yes/no): ")
        if answer == "yes":
            print("You talk to the stranger and you win.")
        elif answer == "no":    
            print("You ignore him and you lose.")
        else:
            print("Not a valid option. You lose")    

    elif answer == "walk back":
        print ("You lose you coward.")
        
    else:
        print("Not a valid option. You lose.")


else:
    print("Not a valid option. You lose.")        

print("Thankyou for trying ", name)
