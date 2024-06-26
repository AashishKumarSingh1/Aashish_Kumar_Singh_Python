# cook your dish here
for _ in range(int(input())):
    D, d, P, Q = map(int, input().split())
    if 1 <= d <= D <= 10**6 and 1 <= P <= 10**6 and 1 <= Q <= 10**6:
        n = D // d  # Number of complete intervals
        remaining_days = D % d
        
        complete_intervals_sum = d * n * P + d * (Q * n * (n - 1) // 2)
        
        remaining_days_sum = remaining_days * (P + n * Q)
       
        total_money = complete_intervals_sum + remaining_days_sum
        
        print(total_money)
