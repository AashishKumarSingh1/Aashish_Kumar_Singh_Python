# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x,y=map(int,input().split())
        if x in range(2,13) and y in range(1,x):
            total_working_hour=x*4+y
            print(total_working_hour)
