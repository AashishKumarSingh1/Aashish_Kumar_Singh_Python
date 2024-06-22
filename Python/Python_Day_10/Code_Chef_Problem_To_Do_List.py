# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        
        n=int(input())
        ratings = list(map(int, input().split()))
        # print(ratings)
        # count=len(ratings)
        # print(count)
        count=0
       
        # count = sum(1 for rating in ratings if rating < 1000)
        for rating in ratings:
            if rating>=1000:
                count+=1
                
        
        print(count)