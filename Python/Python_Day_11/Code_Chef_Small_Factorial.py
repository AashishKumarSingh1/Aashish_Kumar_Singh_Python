# cook your dish here
t=int(input())
if t>=1 and t<=100 :
    for _ in range(t):
        n=int(input())
        if n>=1 and n<=100:
            facotrial=1 
            for i in range(n,0,-1):
                facotrial*=i 
            print(facotrial)