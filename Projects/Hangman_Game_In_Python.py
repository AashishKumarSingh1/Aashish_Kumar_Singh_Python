import random 
# from collections import counter
words="Apple Mango Banana pineapple kiwi"
words_list=list(words.capitalize().split(' '))

random_word=random.choice(words_list)
user_name=input("Enter your Name: ")

print(f"Good Luck! {user_name}")
print(f"Hint is : Word is one of the Fruit Name!")

min_guess=len(random_word)+random.randint(2,5)

user_guesses=''

board=['_'*len(random_word)]

print('  '.join(map(str,board)))

flag=0

print(f"Total Guesses : {min_guess}")
print()
user_word_count=0

while min_guess!=0:    
    guess=input("Enter your Guess: ")
    min_guess-=1

    if guess in random_word:
        k=random_word.count(guess)
        print(f"{guess} is in the list!")
        user_guesses+=guess
        user_word_count+=k 
    else:
        print(f"{guess} is not in the list!")

    for char in random_word:
        if char in user_guesses:
            print(char,end=' ')
            pass
        else:
            print("_",end=" ")
    print()
    if user_word_count==len(random_word):
        print("You Won the Game!")
        print(f"The word is {random_word}")
        flag=1
    
    print(f"Guess Left : {min_guess}\n")
    
if flag==0:
    print("Better Luck Next Time!")
    print(f"The Guess was{random_word}")


