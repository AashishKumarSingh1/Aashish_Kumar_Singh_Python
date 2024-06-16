repeat = 1
average = 0 
while repeat!=0:
    marks=input("Enter your marks : ")
    marks = int (marks)
    if (marks >= 33):
        average = (average*repeat+ marks )/(repeat+1)

    else:
        print("You have less that 33 marks!")
        break

    repeat = input("Enter 0 if you want to stop marks or any number you want to keep going : ")
    repeat= int ( repeat )


if(average>40):
    print("Hurray , you scored more than 40 percent marks! and the average you scored is : ", average)

else:
    print("You have scored less than 40% marks!")

    
