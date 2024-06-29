#Approach 1
# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    n_arr=[i for i in range(1,n+1)]
    #swapping num 
    for i in range(k):
        if 0 <= i < n and 0 <= n-i-1 < n:
            n_arr[i], n_arr[n-i-1] = n_arr[n-i-1], n_arr[i]

    max_ang=0 
    for i in range(len(n_arr)):
       for j in range(i+1, len(n_arr)):
            if n_arr[i] > n_arr[j]:
                max_ang += 1
    print(max_ang)

#Approach 2 
# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    n_arr=[i for i in range(1,n+1)]
    k=min(k,n//2)
    #swapping num 
    for i in range(k):
        if 0 <= i < n and 0 <= n-i-1 < n:
            n_arr[i], n_arr[n-i-1] = n_arr[n-i-1], n_arr[i]

    max_ang=0 
    for i in range(len(n_arr)):
       for j in range(i+1, len(n_arr)):
            if n_arr[i] > n_arr[j]:
                max_ang += 1
    print(max_ang)

#Approach 3
def f(x): # 3 + 7 + 11 + ... + x
    x = (x+1)//4
    return x*(2*x + 1)
for _ in range(int(input())):
    n, k = map(int, input().split())
    k = min(k, n//2)
    print(2*n*k - f(4*k-1))
# ans = (2n-3) + (2n-7) + ... + (2n-4k+1)