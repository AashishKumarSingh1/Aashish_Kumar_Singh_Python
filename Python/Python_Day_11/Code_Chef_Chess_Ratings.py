# cook your dish here
import math
t=int(input())
if t>=1 and t<=10**4 +1 : 
    for _ in range(t):
        x,y=map(int,input().split())
        if x>=1 and x<=y and y<=10**4 :
            match_won=(y-x)/8
            print(math.ceil(match_won))