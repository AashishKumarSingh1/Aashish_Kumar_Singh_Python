# cook your dish here
import math
t=int(input())
if 1<=t<=(10**4):
    for _ in range(t):
        x,y,r=map(int,input().split())
        if 1<=x<=100 and 1<=y<=10 and 0<=r<=3*(10**4) and r%30==0:
            eat_stick=x+r//30 
            plate=math.ceil(eat_stick/y)
            print(plate)
            
            