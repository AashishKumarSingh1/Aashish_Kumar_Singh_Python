# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        a,b,c=map(int,input().split())
        if 1<=(a and b and c)<=1000000:
            num=[a,b,c]
            num.sort()
            print(num[1])
            