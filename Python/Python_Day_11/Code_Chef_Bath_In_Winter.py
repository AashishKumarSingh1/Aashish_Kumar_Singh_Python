# cook your dish here
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        x,y=map(int,input().split())
        if (x and y) in range(1,101):
            print(x//(2*y))