#modified code : : => 
# cook your dish here
t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    if l>=(r-l+1):
        print(r)
    else:
        print(-1)

#unmodified best version of code : 
# cook your dish here
# for _ in range(int(input())):
#     l,r=map(int,input().split())
#     if l==1:
#         print('-1')
#     elif l>1:
#         n=r  
#         l_old=l
#         while True:
#             rem_lists=[(n%(l+i)) for i in range(0,r-l+1)]
#             rem_sort_list = sorted(rem_lists, reverse=True)
#             if rem_lists==rem_sort_list:
#                 break
#             n-=1
#         print(n)
#     else:
#         print('-1')
    

#unmodified code ::=>
# # cook your dish here
# for _ in range(int(input())):
#     l,r=map(int,input().split())
#     # l<n<r  :: n%l>n%l+1 > n%l+2  ... > n%r  
#     #r r-1 r-n if 
#     #check base condition 
#     if l==1:
#         print('-1')
#     elif l>1:
#         n=r  
#         l_old=l
#         count=0
#         while l<r+1 and n!=1:
    
#             current_rem=n%l 
#             next_rem=n%(l+1)
#             if current_rem>next_rem and l!=r :
#                 count+=1
#                 if count==r-l_old:
#                     break
#                 l+=1 
#                 pass
#             else:
#                 count=0
#                 n-=1 
#                 l=l_old
           
#         print(n)
#     else:
#         print('-1')
    