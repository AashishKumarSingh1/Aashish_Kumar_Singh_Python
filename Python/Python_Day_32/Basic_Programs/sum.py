def calc_sum(n:int)->int:
    if n==1:
        return 1
    return calc_sum(n-1)+n

print(calc_sum(10))