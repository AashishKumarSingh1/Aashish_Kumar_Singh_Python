num=int(input("Enter the number : "))
ori_num=num
binaryList=[]
def Binary_Conversion(num):
    while num!=0:
        binaryList.append(num%2)
        # print("hello")
        #to escape from infinite loop
        num=num//2
Binary_Conversion(num)
# ' '.join(binaryList) => with this method we are joining the whole strings and seeing the whole string at once
# ''.join(map(str,binaryList)) => with this method we are joining the every list elements as a string and then joining.

count_one=' '.join(map(str,binaryList)).count('1')
# print(count_one,binaryList)

if(count_one%2==0):
    print(f"The {ori_num} is a Evil Odious Number!")
else:
    print(f"The {ori_num} is not a Evil Odious Number!")

    