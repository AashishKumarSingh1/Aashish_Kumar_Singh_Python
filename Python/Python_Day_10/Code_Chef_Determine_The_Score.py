# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x,n=map(int,input().split())
        if x in range(10,201) and n>=0 and n<=10 and x%10==0:
            print(x//10 * n)