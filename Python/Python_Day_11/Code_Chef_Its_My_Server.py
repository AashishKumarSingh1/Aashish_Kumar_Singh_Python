# cook your dish here
t=int(input())
if t>=1 and t<=200:
    for _ in range(t):
        p,q=map(int,input().split())
        if (p and q)>=0 and (p and q)<=10:
            if (p+q+1)%4==1 or (p+q+1)%4==2:
                print('Alice')
                pass
            else:
                print("Bob")
            #alice bob
            # 12 34 
            # 56 78 
            # 9,10 11,12