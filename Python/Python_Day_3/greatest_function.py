list=[]
for i in range(0,3):
    n1=int(input("Enter the number : "))
    list.append(n1)
    # print(list)

def greatest(List=[]):
    max=0
    for value in List:
        if(value>max):
            max=value
        else:pass

    return max

max=greatest(list)
print(f"The max of all the entered number is : {max}")