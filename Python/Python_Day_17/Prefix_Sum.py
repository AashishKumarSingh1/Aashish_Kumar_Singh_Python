#Approach 1
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n//2<=1:
        print("No")
    else:
        print('Yes')
        sum_n=n*(n+1)//2
        mean=sum_n//n
        a=[mean+i for i in range(1,n+1) ]
        b=[mean-i for i in range(0,n,1) ]
        print(' '.join(map(str,a)))
        print(' '.join(map(str,b)))

#Approach 2
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n//2<=1:
        print("No")
    else:
        print('Yes')
        group_arr=[(i,n-i+1) for i in range(1,(n//2 )+1)]
        f_group_arr=group_arr[:len(group_arr)//2]
        l_group_arr=group_arr[len(group_arr)//2 :]
        
        formatted_f_group_arr = ['{} {}'.format(x, y) for x, y in f_group_arr]
        formatted_l_group_arr = ['{} {}'.format(x, y) for x, y in l_group_arr]

        print(' '.join(formatted_f_group_arr))
        print(' '.join(formatted_l_group_arr))
        # print(f_group_arr,l_group_arr)
        # print(' '.join(map(str,map(str,f_group_arr))))
        # print(' '.join(map(str,map(str,l_group_arr))))

#Approach 3
#cook your dish here
for _ in range(int(input())):
        n = int(input())
        if n % 4 != 0:
            print("NO")
        else:
            print("YES")
            A = []
            B = []
            for i in range(1, n//4 + 1):
                A.append(i)
                A.append(n - i + 1)
            for i in range(n//4 + 1, n//2 + 1):
                B.append(i)
                B.append(n - i + 1)
            print(' '.join(map(str, A)))
            print(' '.join(map(str, B)))

#Same Approach but in different manner 
#cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n%4==0:
        print("YES")
        for i in range(1,n//4+1):
            print(i,end=" ")
        for i2 in range(n,n-n//4,-1):
            print(i2,end=" ")
        print()
        for i3 in range(n//4+1,n//2+1):
            print(i3,end=" ")
        for i4 in range(n//2+1,n-n//4+1):
            print(i4,end=" ")
        print()
    else:
        print("NO")