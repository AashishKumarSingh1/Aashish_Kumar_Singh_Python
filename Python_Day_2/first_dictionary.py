dictionary={
    "namaste":"Greetings",
    "name":"Aashish Kumar Singh",
    "DOB":"8 August , 2004",
}
update = input("Are you interested to enter any new key value pair (y/n):" )
again=1
while again==1:
    if update.startswith('y'):
        pair_key=input("Enter your key name : ")
        pair_value=input("Enter your key value : ")
        dictionary.update({pair_key:pair_value})
        again = input("Are you interested in again storing some new value(y/n) : ")
        if again.startswith('y'):
            again=1
        else :
            again=0
    else:
        again=0

 
print(dictionary)


