count=input("How many fruits you want to enter: ")
count=int(count)
fruit=[]
while count!=0:
    name=input("Enter the name of the fruit: ")
    name=name.capitalize()
    fruit.append(name)
    count-=1

print(fruit)