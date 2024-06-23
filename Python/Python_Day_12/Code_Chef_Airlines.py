# cook your dish here
import math
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        x,n=map(int,input().split())
        if (x and n )<=(10**6) and (x and n)>=1:
            if (math.ceil(n/100)) <=x:
                print('0')
                pass
            else:
                print(math.ceil(n/100)-x)