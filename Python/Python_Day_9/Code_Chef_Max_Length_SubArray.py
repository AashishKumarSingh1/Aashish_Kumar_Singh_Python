t=int(input())
if t>=1 and t<=10**4 :
    for i in range(t):
        n=int(input())
        if n >=1 and n<=10**4:
            # 3 :: output-> 3
            sum=n*(n+1)/2 
            count=n
            if sum%2==0:
                pass
            else:
                sum-=n
                count-=1
            print(count)
