# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        n,x=map(int,input().split())
        if (n and x ) in range(1,11):
            min_pizza=(n*x)//4
            if (n*x)/4==int((n*x)/4):
                print(min_pizza)
            else:
                print(min_pizza+1)