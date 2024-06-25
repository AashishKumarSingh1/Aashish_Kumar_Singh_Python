for _ in range(int(input())):
    n=int(input())
    arrival_time=list(map(int,input().split()))
    departure_time=list(map(int,input().split()))
    
    max_guest=0 
    count=0
    for i in range(n):
        
        guest=[j for j in range(n) if arrival_time[j]<departure_time[i]<=departure_time[j]]
        count=len(guest)
        if max(max_guest,count)==count:
            max_guest=count
    print(max_guest)