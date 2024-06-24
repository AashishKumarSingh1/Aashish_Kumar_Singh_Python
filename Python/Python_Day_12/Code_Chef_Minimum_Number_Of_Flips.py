# cook your dish here
t=int(input())
if 1<=t<=100:
    for _ in range(t):
        n=int(input())
        l_array=list(map(int,input().split()))
        if 2<=n<=1000 and [True for value in l_array if value==1 or value==-1]:
            if len(l_array)%2==0:
                count_1=l_array.count(1) 
                count_n_1=l_array.count(-1)
                print(abs(count_n_1-count_1)//2)
                
                pass
            else:
                print('-1')