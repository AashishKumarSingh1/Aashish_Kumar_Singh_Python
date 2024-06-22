# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        a,b=map(int,input().split())
        if (a and b ) in range(100,10001) and a%100==0 and b%100 ==0 :
            a_valuation=a*10 
            b_valuation=b*5
            if a_valuation>b_valuation:
                print("FIRST")
            elif a_valuation < b_valuation:
                print('SECOND')
            else:
                print("ANY")