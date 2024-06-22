# cook your dish here
n=int(input())
if n in range(1,101):
    input_list=input()
    num=list(map(int,input_list.split()))
    #num[0]=>A1 and so on...
    even_weapon=0 
    odd_weapon=0
    for list in num:
        if list%2==0:
            even_weapon+=list
        else:
            odd_weapon+=list
    if even_weapon>odd_weapon:
        print("READY FOR BATTLE")
    else:
        print('NOT READY')
        