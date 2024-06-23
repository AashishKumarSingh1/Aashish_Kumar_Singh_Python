# cook your dish here
import math
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        n,k,m=map(int,input().split())
        if (n and k and m)>=1 and (n and k and m)<=100:
            print(math.ceil(n/(k*m)))