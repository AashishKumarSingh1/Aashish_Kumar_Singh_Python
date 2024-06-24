# cook your dish here
t=int(input())
if 1<=t<=10:
    for _ in range(t):
        n=int(input())
        code=list(input().split())
        start38=code.count('START38')
        print(start38,n-start38)