# cook your dish here
import math
t=int(input())
if t>=1 and t<=2000:
    for _ in range(t):
        a,b,x,y=map(int,input().split())
        if ( a and b)>=20 and (a and b)<=40 and (x and y)>=0 and (x and y)<=20:
            if x!=0 and (b>=a and (b-a)<=x):
                print('Yes')
                pass
            elif y!=0 and (b<=a and (a-b)<=y):
                print('Yes')
                pass
            elif a==b:
                print('Yes')
                pass
            
            else:
                print('No')
            
                
            #a b x y     
            # b-a 
            # 1 -1 