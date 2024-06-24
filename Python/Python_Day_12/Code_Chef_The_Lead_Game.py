# cook your dish here
n=int(input())
if n<=10000:
    s,t=0,0
    leader=0 
    lead_1=0 
    lead_2=0
    
    for _ in range(n):
        
        s_n,t_n=map(int,input().split())
        s+=s_n
        t+=t_n
        if s>t:
            leader=1 
            if lead_1<(s-t):
                lead_1=s-t 
                pass
        elif t>s:
            leader=2 
            if lead_2<(t-s):
                lead_2=t-s
                pass
        else:
            pass
    if max(lead_2,lead_1) == lead_1:
        print("1",lead_1)
        pass
    else:
        print("2",lead_2)
            
        