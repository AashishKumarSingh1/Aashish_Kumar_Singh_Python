number = int(input("Enter the number : "))

# def quadratic(num):
#     n1=(-1+(pow(1+4*number,0.5)))//2
#     n2=(-1-(pow(1+4*number,0.5)))//2
#     n1,n2=max(n1,n2),min(n1,n2)
#     if(n1==n2+1):
#         return True
#     else:
#         return False

for i in range(1,number//2+1):
    if(number%i==0):
        if(number%(i+1)==0):
            if(i*(i+1)==number):
                print(f"The {number} is a Pronic Number!")
                number=0
                break
else:
    print("Done!")

if(number):
    print(f"The {number} is not a Pronic Number!")

