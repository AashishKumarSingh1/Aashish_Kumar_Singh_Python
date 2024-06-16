#this program is going to print the table of any number entered by the user and upto any specified row

table=int(input("Enter which number table you want to print : "))

upto=int(input("Enter upto which number you want your table :"))

for i in range(1 , upto+1):
    print(f"{table} * {i} = {table*i}")
    i+=1


