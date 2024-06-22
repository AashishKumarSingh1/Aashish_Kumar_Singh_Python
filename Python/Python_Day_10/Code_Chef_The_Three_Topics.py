# cook your dish here
a,b,c,x = map(int,input().split())
if (a and b and c and x ) in range(1,11) and a!=b and b!=c and a!=c :
    list=[a,b,c]
    if x in list:
        print("Yes")
    else:
        print("No")