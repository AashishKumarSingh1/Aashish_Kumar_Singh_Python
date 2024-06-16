#this program is going to check that whether a username is having 10 character or not 

username=str(input("Enter your username: "))
username_count=len(username)
if(username_count<10):
    print(f"The '{username}' has less than 10 characters! ")

else:
    print(f"The {username} is in the proper format!")