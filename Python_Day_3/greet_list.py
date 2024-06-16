l1=["Aashish","Aadarsh","Hello","Kaju","Kismis"]


for keyword in l1:
    if(keyword in l1 and keyword.startswith('A')):
        print(f"Greetings {keyword}")

else:
    print("Done!")