t=int(input())
if t>=1 and t<=1000:
     for _ in range(t):
         a,b,c=map(int,input().split())
         
         if a>=1 and b>=1 and c>=1 and a<=10 and b<=10 and c<=10:
             
             
            if ((a+b)/2>c):
                 print('YES')
            else:
                 print('NO')
     
