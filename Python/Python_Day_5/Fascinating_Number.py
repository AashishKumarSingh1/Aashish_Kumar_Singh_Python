num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:#or i can use => len(str(num))==3

    concatenated_num = str(num) + str(num * 2) + str(num * 3)

    if sorted(concatenated_num) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print(f"{num} is a fascinating number!")
    else:
        print(f"{num} is not a fascinating number.")
else:
    print(f"The number {num} is not a 3-digit number!")


