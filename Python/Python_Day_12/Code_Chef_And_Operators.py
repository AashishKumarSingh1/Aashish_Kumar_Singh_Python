# cook your dish here
t=int(input())
if 1<=t<=10000:
    for _ in range(t):
        a,b=map(int,input().split())
        if 1<=(a and b)<=10000000001:
            if a>b:
                print(">")
                pass
            elif a<b:
                print("<")
                pass
            elif a==b:
                print('=')
                pass
            else:
                pass
            