# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m,t=[],[]
    for i in range(n):
        if(i%2==0):
            m.append(l[i])
        else:
            t.append(l[i])
    i=0
    while(i<k):
        a=max(m)
        b=min(t)
        m.remove(a)
        t.append(a)
        t.remove(b)
        m.append(b)
        i+=1
    if(sum(m)<sum(t)):
        print('YES')
    else:
        print('NO')
            """"
            def custom_sum(lst):
    total_sum = 0
    for i in range(len(lst)):
        total_sum += lst[i]
    return total_sum

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    m_list = [a[i] for i in range(n) if (i + 1) % 2 == 0]
    t_list = [a[i] for i in range(n) if i % 2 == 0]

    m_list.sort() 
    t_list.sort()  

    for i in range(min(k, n)):
        m_list[-1 - i], t_list[i] = t_list[i], m_list[-1 - i]

    m_list_sum = custom_sum(m_list)
    t_list_sum = custom_sum(t_list)

    if m_list_sum >= t_list_sum:
        print("no")
    else:
        print("yes")

            
            """