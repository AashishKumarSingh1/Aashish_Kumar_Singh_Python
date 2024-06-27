# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    #x1 x2 x3 .... => sum=(x1+x2+x3...) -xi = ai 
    # sum = 3(a1+a2+a3...)/2n
    #sum_vairable*n - (x1 x2 ....)=(a1 a2 a3...)
    #sum_vairable*n-sum=(a1+a2+a3...)
    #xi=sum-ai 
    
    sum_a=sum(a)
    sum_vairable=(sum_a)/(n-1)
    xi=[int(sum_vairable-a[i]) for i in range(n)]

    print(' '.join(map(str,xi)))