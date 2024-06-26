#importing random module 
import random 


words=["Aashish","Kumar","Singh"]
random_word=random.choice(words)

user_name=input("Enter your Name: ")
print(f"Good Luck {user_name}")

word_box=['_ '*len(random_word)]
print(' '.join(map(str,word_box)))

min_guess=len(random_word)+random.randint(1,5)
guesses=''
print("Total Guess : ",min_guess )
print(f"""
Words are chosen from the list : {words}
""")
while min_guess>0:
    user_guess=input(f"Hlo ,{user_name} What will you Guess! ")
    min_guess-=1
    print(f"You have {min_guess} Guesses left!")
    
    if user_guess in random_word:
        print("You Got it!")
        guesses+=user_guess
        pass
    else:
        print("Better luck next Time!")
        pass
    for char in random_word:
        if char in guesses:
            print(char,end=" ")
            pass
        else:
            print("_",end=" ")
            pass
    print()
    if random_word in guesses:
        print("Hurray! You Win the Game!")
        break
    print()




