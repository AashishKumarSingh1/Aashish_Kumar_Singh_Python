T=int(input())
if T>=1 and T<=21000:
    for i in range(1,T+1):
        A,B,X=map(int,input().split())
        if A>=100 and B>A and B<=200 and X<=50 and X>=1:
            time=(B-A)//X
            print(time)
        else:
            pass
    
else:
    pass

    
