# cook your dish here
t=int(input())
if t in range(1,201):
    for _ in range(t):
        n , x=map(int,input().split())
        persons_age=list(map(int,input().split()))
        voters=0 
        for voter in persons_age:
            if voter>=x :
                voters+=1 
            
        print(voters)