# cook your dish here
n,m=map(int,input().split())
x,y=map(int,input().split())

if (n and m) in range(0,101) and (x and y) in range(0,1001):
    print(n*x + m*y)