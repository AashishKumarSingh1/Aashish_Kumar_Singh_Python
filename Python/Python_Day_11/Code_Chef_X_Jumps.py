# cook your dish here
t=int(input())
if t>=1 and t<=500:
    for _ in range(t):
        x,y=map(int,input().split())
        if (x and y) >=1 and (x and y)<=100:
            print(x//y+x%y)