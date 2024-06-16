import random
for i in range(1,5):
    gamePlay=["Snake","Water","Gun","I will choose Mota Bhai!","He Ke Ke Ke!","Dekh Beta mai rai dunga east or west B-Tech is the best chaar saal me ho jaega!","He Ke Ke Ke!","Dekh Beta mai rai dunga east or west B-sc is the best teen saal me ho jaega!"]

    user_input=str(input("Enter your turn (Snake , Water , Gun ): "))
    user_input=user_input. capitalize()

    def random_selector(gamePlay=[]):
        return random.choice(gamePlay)

    computer_select=random_selector(gamePlay)
    print(f"Computer Selects : {computer_select}")
    if(computer_select==user_input):
        print("The computers and users both wins the match!")

    elif computer_select=='Snake' and user_input=="Gun":
        print("User wins the game!")

    elif computer_select=='Water' and user_input=="Snake":
        print("User wins the game!")

    elif computer_select=="Gun" and user_input=="Snake":
        print("Computer wins the game!")

    elif user_input not in gamePlay:
        print(f"You have choosed {user_input} which is not a rule of the game!")

    else:
        print("Aashish wins the game!")

else:
    print("This Game is Over!")
