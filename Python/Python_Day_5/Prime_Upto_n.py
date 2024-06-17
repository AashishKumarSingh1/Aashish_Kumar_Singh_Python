num=int(input("Enter the number : "))

def PrimePrinter(num):
    prime=1
    for i in range(2,num):
        if num%i==0:
            prime=0
            return prime
        
    else:
        print(f"{num}")
        return prime
    
for i in range(2,num+1):
    PrimePrinter(i)



    
