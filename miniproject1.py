print("Welcome To My Quizz!")

playing = input("Are you smart enough? ")

if playing.lower() != "yes":
    print("Ohh,What a Shame")
    quit()

print("Okay! Let's Play :)")
score = 0


answer = input("What is the full form of cpu? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! :(")


answer = input("Who won the 2022 world cup? ")
if answer.lower() == "argentina":
    print('Correct')
    score += 1
else:
    print("Incorrect! :(")


answer = input("Who is the mayor of Kathmandu? ")
if answer.lower() == "balen":
    print('Correct!')
    score += 1
else:
    print("Incorrect! :(")        


answer = input("What is the megapixel of a human eye? ")
if answer.lower() == "576 megapixel":
    print('Correct!')
    score += 1
else:
    print("Incorrect! :(")
        
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100)+ " %.")


