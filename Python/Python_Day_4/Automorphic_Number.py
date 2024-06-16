num=int(input("Enter the number : "))

sqr_num=pow(num,2)

is_auto_num=str(sqr_num).endswith(str(num))

if(is_auto_num):
    print(f"The {num} is Automorphic Number!")

else:
    print(f"The {num} is not a Automorphic Number!")
