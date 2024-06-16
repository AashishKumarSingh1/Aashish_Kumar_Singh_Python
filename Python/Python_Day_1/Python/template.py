import datetime

name = input("Enter your name: ")
#formatted string 
letter = f"""Dear {name},

Congratulations! You are selected!

Date: {datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")}

Best regards,
Aashish Kumar Singh

"""

print(letter)
