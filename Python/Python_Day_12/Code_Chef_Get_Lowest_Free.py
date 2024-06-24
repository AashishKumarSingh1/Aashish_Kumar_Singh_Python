# cook your dish here
t=int(input())
if 1<=t<=100:
    for _ in range(t):
        a,b,c=map(int,input().split())
        if 1<=(a and b and c)<=10:
            pay_amount=a+b+c-min(a,b,c)
            print(pay_amount)