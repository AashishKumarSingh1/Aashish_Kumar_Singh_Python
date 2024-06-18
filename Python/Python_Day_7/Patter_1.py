
no_row=int(input("Enter the no. of row : "))
triangle=[]
for i in range (1,no_row+1):
    row=[]
    for j in range(1,no_row+1):
        row.append("*")
    triangle.append(row)
else:
    print("Done!")
print(triangle)
print("Pattern=>")
pattern=" ".join(map(str,triangle))
for row in triangle:
    print(row)
    pattern=" ".join(row)
    print(pattern)
# print(pattern)
