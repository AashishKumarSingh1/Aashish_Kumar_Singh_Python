year = int(input("Enter the year: "))

if (year%400==0 or (year%4==0 and year%100!=0)):
    print(f"The {year } is a leap Year!")

else:
    print(f"The {year} is not a leap Year!")

