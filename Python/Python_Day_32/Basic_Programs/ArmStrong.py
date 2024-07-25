def isArmstrong(num:int)->bool:
    digit_cube_sum=0 
    ori_num=num
    while num>0:
        digit_cube_sum+=pow(num%10,3)
        num=num//10
        print(digit_cube_sum)
    if ori_num==digit_cube_sum:
        return True
    else:
        return False

print(isArmstrong(663))

