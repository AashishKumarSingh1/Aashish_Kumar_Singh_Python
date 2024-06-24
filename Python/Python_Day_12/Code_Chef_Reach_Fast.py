# cook your dish here
import math
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        a,b,k=map(int,input().split())
        if 1<=a<=100 and 1<=b<=100 and 1<=k<=100:
            steps=abs(b-a)//k+(b-a)%k
            if abs(a-b)<k and a!=b:
                print("1")
                pass
            else:
                steps=(abs(a-b)//k )
                if (a-b)%k==0:
                    pass
                else:
                    steps+=1
                print(steps)
                pass
