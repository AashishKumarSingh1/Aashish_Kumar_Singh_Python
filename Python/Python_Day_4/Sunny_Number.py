import math
num=int(input("Enter the number : "))

# if str(pow((num+1),0.5)/10).endswith('.0'):
#     print(f"The {num} is a Sunny Number!")

# else:
#     print(f"The {num} is not a Sunny Number!")

# x=math.sqrt(num+1)
x=pow((num+1),0.5)
if int(x)==x:
    print(f"The {num} is a Sunny Day!")
else:
    print(f"The {num} is not a Sunny Day!")
