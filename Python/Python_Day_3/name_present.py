name=["Aashish","Kumar","Singh"]
user_name=str(input("Enter your name: "))
for keyword in name:
    if keyword in user_name:
        print(f"{keyword} is present in {user_name}")
        break
    else:
        print("No keyword was detected!")