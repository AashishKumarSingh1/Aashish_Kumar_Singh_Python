######################################## METHOD ::=> 1
t = int(input())
if 1 <= t <= 10**5:
    # results = []
    for _ in range(t):
        a, b, c, d, k = map(int, input().split())
        if 0 <= a <= 10**5 and 0 <= b <= 10**5 and 0 <= c <= 10**5 and 0 <= d <= 10**5 and (a, b) != (c, d) and 1 <= k <= 2*10**5:
            # Calculate the Manhattan distance
            distance = abs(a - c) + abs(b - d)
            # Check if it's possible to reach in exactly k steps
            if distance <= k and (k - distance) % 2 == 0:
                # results.append("YES")
                print('YES')
            else:
                print('NO')
                # results.append("NO")
#################################### METHOD :: => 2
    # Print all results
    # for result in results:
    #     print(result)

# t=int(input())
# if t>=1 and t<=10**5:
#     for _ in range(t):
#         a,b,c,d,k=map(int,input().split())
#         if a>=0 and b>=0 and c>=0 and d >=0 and a<=10**5 and b<=10**5 and c<=10**5 and d<=10**5 and (a,b)!=(c,d) and k>=1 and k<=(2*10**5):
#             #1 1 2 2 2 :: YES 
#             #a b c d k 
#             step=0
#             while b!=d and a!=c:
#                 if min(b+1,d)>min(b-1,d):
#                     b=b-1
#                     step+=1 
#                 else:
#                     b=b+1
#                     step+=1
                
#                 if min(a+1,c)>min(a-1,c):
#                     a=a-1 
#                     step+=1
#                 else:
#                     a+=1
#                     step+=1
                
#                 if(step>k):
#                     # print("NO")
#                     break
#             if step==k:
#                 print('YES')
#             else:
#                 print(step,k)
#                 print('NO')
            
            
            
            
            

            
            
            
        
    