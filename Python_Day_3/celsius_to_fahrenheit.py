temp=int(input("Enter the temperature in degree celsius : "))

def celsius_to_fahrenheit(temp):
    f = 9/5*temp+32
    return f

c_to_f=celsius_to_fahrenheit(temp)
print(f"The degree conversion of {temp}C to fahrenheit is : {c_to_f}F")
