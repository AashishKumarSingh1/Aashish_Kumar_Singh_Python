#Approach 1
# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    sum_mean=x*n 
    array=['None']*(n-1)
    array=[i+1 for i in range(len(array))]
    # array[0]=sum_mean//2
    array.append(sum_mean-sum(array))
    print(' '.join(map(str,array)))

#Approach 2
T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    
    if n % 2 == 1:
        print(x, end = ' ')
    
    for i in range(n // 2):
        print(x - (i + 1), x + (i + 1), end = ' ')
    print()