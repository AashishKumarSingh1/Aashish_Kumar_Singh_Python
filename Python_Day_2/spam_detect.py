set={"make a lot of money","buy now","subscribe this","Click This"}
message = input("Enter your message : ")

if(set.union(message).issuperset(set)):
    print("Entered message is spam!")

else:
    print("Entered message is not spam!")