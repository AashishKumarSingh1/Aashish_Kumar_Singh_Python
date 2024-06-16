repeat=1
while repeat:
    


    option = input("""1)Enter 1 if you want to see the list of entered numbers
2)Enter 2 if you want to only store the number
""") 
    option=int(option)
    s={}
    if option==1:
        print(f"""The values are : 
            {s} """)
        repeat=0

    elif option==2:
        number=input("Enter the number you want to store : ")
        number=int(number)
        s.update(number)
    
