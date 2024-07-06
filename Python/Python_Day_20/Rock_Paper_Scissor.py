import random 
def Choices():
    player_choice=input("Enter Your Choice ( Rock , Paper , Scissors : ) : ")
    choices=['Rock','Paper','Scissors']
    computer_choice=random.choice(choices)
    choice_list={
        'Player_choice':player_choice,
        'Computer_choice':computer_choice
    }
    return choice_list

def check_win(player,computer):
    if player==computer:
        return "It's a Tie!"
    elif player=='Rock':
        if computer=='Paper':
            return "Computer Wins! Computer chooses Paper, You chose : Rock!"
        elif computer=='Scissors':
            return "Rock Wins Over Scissors! Computer Choses Scissors!"
    elif player=='Paper':
        if computer=='Rock':
            return "Player Wins! Computer chooses Rock, You chose : Paper!"
        elif computer=='Scissors':
            return "Scissors Wins Over Paper! , Computer Wins! Computer Choses Scissors!"
    elif player=='Scissors':
        if computer=='Paper':
            return "Player Wins! Computer chooses Paper, You chose : Scissors!"
        elif computer=='Rock':
            return "Rock Wins Over Scissors! Computer Wins! Computer Choses Rock!"
    else:
        return f"Player Choses{player} and Computer Choses{computer}"

list_choice=Choices()
winning=check_win(list_choice['Player_choice'],list_choice['Computer_choice'])
print(winning)