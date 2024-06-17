num=int(input("Enter the number : "))

cube_num=pow(num,3)

if(str(cube_num).endswith(str(num))):
    print(f"The {num} is a Trimorphic Number!")
else:
    print(f"The {num} is not a Trimorphic Number!")