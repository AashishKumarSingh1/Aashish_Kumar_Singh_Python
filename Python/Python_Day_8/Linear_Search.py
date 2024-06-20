# Linear Search

numList=[1,2,3,4,5,6,7,8,9,10]
print("List has the items : ",numList)

searchNum=int(input("Enter the number to search for : "))
found=False

for i in range(len(numList)):
    if searchNum==numList[i]:
        
        found=True
    if found==True:
        break
    

else:
    print("Done!")
if found==True:
    print(searchNum,  " is found in the list!")
else:
    print(searchNum," is not found in the list!")