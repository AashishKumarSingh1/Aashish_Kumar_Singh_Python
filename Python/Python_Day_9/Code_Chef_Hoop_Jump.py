t=int(input())
if t in range(1,(pow(10,5))+1):
    for i in range(t):
        n=int(input())
        if n in range(1,(2*pow(10,5))+1):
            last_hoop=(n+1)//2
            print(last_hoop)
        else:
            pass
else:
    pass

    
