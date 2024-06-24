# cook your dish here
t=int(input())
if 1<=t<=10**4:
    for _ in range(t):
        a1,a2,a3,b1,b2,b3=map(int,input().split())
        if 1<=(a1 and a2 and a3 and b1 and b2 and b3)<=6:
            alice_score=a1+a2+a3-min(a1,a2,a3)
            bob_score=b1+b2+b3-min(b1,b2,b3)
            if alice_score>bob_score:
                print("Alice")
                pass
            elif bob_score>alice_score:
                print("Bob")
                pass
            else:
                print("Tie")