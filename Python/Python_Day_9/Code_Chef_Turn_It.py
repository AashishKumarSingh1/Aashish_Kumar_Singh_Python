t=int(input())
if t>=1 and t<=10**5 :
    for i in range(t):
        u,v,a,s=map(int,input().split())
        if u>=1 and u <=10**4 and v >=1 and v<=10**4 and a>=1 and a<=10**4 and s>=1 and s<=10**4 :
            #1 1 1 1 :: yes
            V=pow(u**2-2*a*s,0.5)
            if float(v) < float(V.real):
                print("No")
            else:
                print("Yes")