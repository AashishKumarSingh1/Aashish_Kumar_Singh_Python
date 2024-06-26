import random 

words=["Aashish",'Kumar',"Singh"]

word=random.choice(words)

print("""
Welcome User!
This is the game of word guessing
choices are => 
            1)Aashish
            2)Kumar
            3)Singh
::=> Enter the character one by one!
""")
for char in word:
    print('_',end=" ")
turns=15 
guesses=''
length=len(set(word))

print()
while turns!=0:
    guess=input("\nEnter the character : ")
    if len(guess)>1:
        print(f"\nYou have entered {len(guess)} character!\nPlease enter one character at a time!\n")
        continue
    turns-=1 
    guesses+=guess
    fill=0
    for char in word: 
        if char in guesses:
            fill+=1
            print(char,end=" ")
        else:        
            print("_",end=" ")
        
    print()
    if guess not in word:
        print()
        print("Wrong Guess!")
        print()

    if fill==len(word):
        print("You Win the Game!")
        print("The Guess was : ",word)
        break
print()
print("Thankyou!")
print()

        

    

