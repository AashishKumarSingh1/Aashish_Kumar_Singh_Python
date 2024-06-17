def Fascinating_Number(num):
    list_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    con_num = str(num) + str(num * 2) + str(num * 3)
    if sorted(con_num) == list_digits:
        return True
    else:
        return False

num = int(input("Enter the number: "))
print(f"The Fascinating Numbers from 100 to {num} are:")
for i in range(100, num + 1):
    if Fascinating_Number(i):
        print(i)
else:
    print("Done!")
