# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        n=int(input())
        if n in range(1,(10**6)+1):
            profit=50*n-(20/100)*50*n-(20/100)*50*n-(30/100)*50*n 
            print(int(profit))