t=int(input())
if t>=1 and t<=101:
    for _ in range(t):
        n,m=map(int,input().split())
        #2,3
        if n>=1 and n<=100 and m>=0 and m<=100:
            # left_shoe=m 
            # friends=n 
            if n>m:
                # req_left_shoe=(n-m)+n
                print(n-m+n)
                pass
            else:
                # req=n
                print(n)
            # if m>=2*n:
            #     print(n)
            #     pass
            # else:
            #     extra_shoe=abs(n-m)+n 
            #     print(extra_shoe)