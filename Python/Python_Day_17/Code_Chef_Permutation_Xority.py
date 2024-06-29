#Approach 1
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    n_arr=[]
    if n%2==0:
        n_arr=[i for i in range(1,n+1)]
    elif n%2!=0:
        n_arr=[2,3,1]
        for i in range(4,n+1):
            n_arr.append(i)
        
    elif n==2:
        n_arr=['-1']
    else:
        pass
    print(' '.join(map(str,n_arr)))

#Approach 2
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(-1)
    else:
        a = list(range(1, n + 1))
        if n % 2 == 0:
            a.insert(1, n)
            a = a[:-1]
        print(*a)