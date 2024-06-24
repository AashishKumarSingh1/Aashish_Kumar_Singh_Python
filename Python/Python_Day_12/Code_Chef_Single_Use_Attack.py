import math
# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        h,x,y=map(int,input().split())
        if 1<=x<y<=h<=100:
            step=0 
            h=h-y 
            step+=1 
            # while h!=0:
            #     h=h-x 
            #     step+=1 
            step+=math.ceil(h/x)
            print(step)
                