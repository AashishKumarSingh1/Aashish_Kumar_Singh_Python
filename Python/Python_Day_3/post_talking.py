post=str(input("Enter your post : "))

name=["Aashish Kumar Singh","Aashish"]


for keyword in name:
    if keyword in post:
        post.capitalize
        print(f"The {post} is talking about Aashish Kumar Singh!")
        break

    else:
        print(f"The {post} is not talking about Aashish Kumar Singh!")

