# cook your dish here
t=int(input())
if t>=1 and t<=1001:
    for _ in range(t):
        x,y=map(int,input().split())
        if x>=0 and y>=0 and x<=100 and y<=100:
            print(max(x,y))