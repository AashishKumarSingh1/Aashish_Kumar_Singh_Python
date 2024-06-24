# cook your dish here
import math
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        n=int(input())
        if 1<=n<=1000:
            print(math.ceil(n/10))
        