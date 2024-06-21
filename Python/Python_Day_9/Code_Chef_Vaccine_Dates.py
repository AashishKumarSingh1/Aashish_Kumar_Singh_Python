t=int(input())
if t>=1 and t<=pow(10,5):
    for i in range(t):
        d,l,r=map(int,input().split())
        if d>=1 and d<=pow(10,9) and l>=1 and l<=pow(10,9) and r>=l and r<=pow(10,9):
            if d in range(l,r+1):
                print("Take second dose now")
            elif d in range(l+1):
                print("Too Early")
            elif d>r:
                print("Too Late")
            else:
                pass
            
        else:
            pass

else:
    pass
    
