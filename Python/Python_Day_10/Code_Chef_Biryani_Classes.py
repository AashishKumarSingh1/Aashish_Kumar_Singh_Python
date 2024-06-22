# cook your dish here
t=int(input())
if t in range(1,10**4 +1):
    for _ in range(t):
        x,y =map(int,input().split())
        if (x and y) in range(1,101):
            print(x*y)