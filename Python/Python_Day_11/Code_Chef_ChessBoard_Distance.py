# cook your dish here
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        x1,y1,x2,y2=map(int,input().split())
        if (x1 and x2 and y1 and y2) in range(1,10**5 +1):
            print(max(abs(x1-x2),abs(y1-y2)))