name = input("Enter your name: ")
dblSpace = name.find("  ")

# print(dblSpace)

if dblSpace != -1:
    print("In the name", name, "there is double space!")
    #replacing double space with single space
    newName=name.replace("  "," ")
    print("After the replacement of double space of ",name ,"\nIt has been changed to : ", newName)
else:
    print("In the name", name, "there is not any double space!")


