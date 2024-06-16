count=input("Enter how many marks you want to enter: ")
count=int(count)
marks=[]

while count!=0:
    mark=input("Enter your marks: ")
    mark=int(mark)
    marks.append(mark)
    count-=1

marks.sort()
print(marks)
