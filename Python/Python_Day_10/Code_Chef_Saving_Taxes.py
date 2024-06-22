# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x,y=map(int,input().split())
        print(x-y)