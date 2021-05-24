import random


print( "For snake press 's'\n"
      "For water press 'w'\n"
      "For Gun press 'g'")

Bot_Score = 0 # computer score
user_score = 0 #user score
chance = 10 #life
while True:
    chance = chance - 1
    print("Life",chance)

    if chance == 0:
        print("Your Score :",user_score , "Computer Score :",Bot_Score)
        if user_score > Bot_Score:
            print(" Congratulation You Won")
        elif user_score < Bot_Score:
            print(" Sorry You Lose")
        else:
            print("Its a Tie")
        print("Game Over")
        exit()
    components = ["s", "w", "g"]
    b = random.choice(components)

    user = input("Please Entre your choice: ")
    if ((user == "s") and (b == "s")):
        print("Tie")
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)

    elif user == "s" and b == "w":
        print("You win")
        user_score = user_score + 1
        print("Your Score :",user_score , "Computer Score :",Bot_Score)
        print(b)

    elif user == "s" and b == "g":
        print("You Lose")
        Bot_Score = Bot_Score + 1
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)

    elif user == "w" and b == "w":
        print("Tie")
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)

    elif user == "w" and b == "g":
        print("You win")
        user_score = user_score + 1
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)

    elif user == "w" and b == "s":
        print("You Lose")
        Bot_Score = Bot_Score + 1
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)


    elif user == "g" and b == "s":
        print("You win")
        user_score = user_score + 1
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)

    elif user == "g" and b == "w":
        print("You Lose")
        Bot_Score = Bot_Score + 1
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)

    elif user == "g" and b =="g":
        print("Tie")
        print("Your Score :", user_score , "Computer Score :", Bot_Score)
        print(b)
    else:
        print("Please enter a valid input")
        chance = chance+1



