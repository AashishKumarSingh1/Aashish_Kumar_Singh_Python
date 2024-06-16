spam_keywords = ["make a bit of money", "buy now", "subscribe this"]

message = input("Enter your message: ")
message = message.lower()

for keyword in spam_keywords:
    if keyword in message:
        print(f"Warning: '{keyword}' found in the message. This might be spam.")
        break
    else:
        print("This is not a spam!")