#Approach 1
for _ in range(int(input())):
    n = int(input())
    time = list(map(int, input().split()))
    
    min_time = float('inf') 
    sum_time=sum(time)
    if n==1:
        print(time[0])
    else:
        for i in range(1, n): 
            sum_left = sum(time[:i])  # Sum of elements before index i
            # sum_right = sum(time[i:])  # Sum of elements from index i onwards
            time_taken = max(sum_left, sum_time-sum_left)  # Maximum of the two sums
            
            if time_taken < min_time:
                min_time = time_taken
        print(min_time)
        
    
#Approach 2
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    if n == 1:
        print(*a)
    else:
        for i in range(n):
            pre = sum(a[0:i])
            suf = sum(a[i:n])
            res.append(max(pre, suf))
        print(min(res))

#Approach 3 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = s = sum(a)
    c = 0
    for i in a:
        c += i 
        res = min(res, max(c, s-c))
    print(res)

list=['']
