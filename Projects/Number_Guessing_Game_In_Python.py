import random 
import math 
random_number=1 
def random_generator(lower,upper):
    return random.randint(lower,upper)


lower=int(input("Enter lower number : "))
upper=int(input("Enter higher number : "))

min_steps=round(math.log(upper-lower+1,2))

print(f"\nYou have {min_steps} chance to Guess the number!\n")

random_number=int(random_generator(lower,upper))
count=0 

while count<min_steps:
    guess=int(input("Enter your Guess : "))
    if guess==random_number:
        print("Your Guess was accurate!")
        break
    elif guess<random_number:
        print(f"{guess} is smaller, Think of some larger number!")
    elif guess>random_number:
        print(f"{guess} is larger, Think some smaller number!")
    else:
        pass
    if count==min_steps:
        print(f"The guess number was : {guess}!")
        print("Better luck next time!")
    count+=1
    



