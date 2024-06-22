# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        a,b,x,y=map(int,input().split())
        if (a and b and x and y) in range(1,1001):
            if (x*y >= a*b):
                print("Yes")
            else:
                print("No")
