# cook your dish here
import math
t=int(input())
if 1<=t<=10**5:
    for _ in range(t):
        n,a,b=map(int,input().split())
        if 2<=n<=2**20 and 1<=a<=100 and 1<=b<=100 and (n &(n-1))==0:
            total_round=math.log(n,2)
            time_round=a*total_round 
            break_round=total_round-1 
            break_time=break_round*b 
            print(int(break_time+time_round))
            