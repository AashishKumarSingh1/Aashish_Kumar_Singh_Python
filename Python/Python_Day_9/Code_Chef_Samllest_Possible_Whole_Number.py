t = int(input())
if 1 <= t <= 10**5:
    for i in range(t):
        n, k = map(int, input().split())
        if 1 <= n <= 10**9 and 0 <= k <= 10**9:
            if k == 0:
                print(n) 
            else:
                print(n % k) 
