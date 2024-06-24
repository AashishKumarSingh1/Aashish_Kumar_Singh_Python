# cook your dish here
t=int(input())
if 1<=t<=100:
    for _ in range(t):
        n,k=map(int,input().split())
        values=list(map(int,input().split()))
        if 1 <= n <= 100 and 1 <= k <= 100 and all(1 <= value <= 10**5 for value in values):
            values_7=[value for value in values if (value+k)%7==0]
            print(len(values_7))