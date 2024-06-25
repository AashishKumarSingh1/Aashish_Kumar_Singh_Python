# cook your dish here
for _ in range(int(input())):
    n=int(input())
    permutation=[0]*n 
    for i in range(n//2):
        permutation[i]=n-(2*i)
        permutation[-(i+1)]=n-(2*i)-1 
    if n!=0:
        permutation[n//2]=1 
    print(' '.join(map(str,permutation)))
        