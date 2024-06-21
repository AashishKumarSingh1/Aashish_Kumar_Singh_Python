t = int(input())


results = []
for _ in range(t):
    l, r = map(int, input().split())

    count = 2 * r - 2 * l + 1
    results.append(count)

for result in results:
    print(result)

###################################################
t=int(input())
if t >=1 and t<= 10**5 : 
    for _ in range(t):
        l,r=map(int,input().split())
        if l>=1 and l<=r and r>=l and r <=10**6 :
            # print("l: ",l , " r: ",r)
            count=0
            #input: 2 2 :: output: 1 
            count = 2 * r - 2 * l + 1
                
            print(count)

##################################################

# t=int(input())
# if t >=1 and t<= 10**5 : 
#     for _ in range(t):
#         l,r=map(int,input().split())
#         if l>=1 and l<=r and r>=l and r <=10**6 :
#             print("l: ",l , " r: ",r)
#             count=0
#             #input: 2 2 :: output: 1 
#             for sum in range(2*l,2*r+1):
#                 for i in range(l,r+1):
#                     n1=i
#                     n2=sum-n1
#                     if n1 >= l and n1<=r and n2<=r and n2 >=l and n2>=n1 :
#                         count+=1
#                         print(n1,n2)
#                     else:
#                         pass
#             print(count)
                
            

