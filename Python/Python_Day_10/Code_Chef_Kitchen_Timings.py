# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        x,y=map(int,input().split())
        if x>=1 and x<y and y<=12 and y>x:
            print(y-x)
            