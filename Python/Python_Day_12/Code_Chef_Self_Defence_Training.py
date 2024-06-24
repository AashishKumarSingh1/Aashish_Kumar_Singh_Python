# cook your dish here
t=int(input())
if t>=1 and t<=20:
    for _ in range(t):
        n=int(input())
        women_age=list(map(int,input().split()))
        if n>=1 and n<=100:
            # boolean = [True for age in women_age if 1 <= age <= 100]
            boolean = all(1 <= age <= 100 for age in women_age)
            if boolean == True:
                eligible_count=[True for age in women_age if 10<= age <=60]
                count=eligible_count.count(True)
                print(count)
                
                
            
