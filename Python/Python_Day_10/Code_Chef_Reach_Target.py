# cook your dish here
t=int(input())
if t>=1 and t<=10:
    for _ in range(t):
        x,y=map(int,input().split())
        if y>=50 and y<x and x<=200 and x>y:
            print(x-y)