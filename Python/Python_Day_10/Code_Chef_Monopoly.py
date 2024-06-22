# cook your dish here
t=int(input())
if t in range(1,5001):
    for _ in range(t):
        p,q,r,s=map(int,input().split())
        if (p and q and r and s ) in range(1,101):
            max_profit=max(p,q,r,s)
            total_profit=p+q+r+s-max_profit
            if max_profit>total_profit:
                print('YES')
                pass
            else:
                print("NO")
                pass
            
            
            
            