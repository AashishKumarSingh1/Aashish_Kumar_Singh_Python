name=input("Enter the name : ")
print(name)
original_name=name
print("The length of the string ",name , " is" , len(name))
name=name[0:3]
print(name)
print("The length of the string ",name , " is" , len(name))
# str.endswith()
# ending= str.endswith("end")
# print(ending)
#code to check the ending of the variable of string data types 
ending=name.endswith("as")
print(ending)

#code to count the given character 
count=name.count('a')
print(count)

#code to capitalize the string
capital=name.capitalize()
print(capital)

#code to find the index 
find=name.find("as")
print("using of find method is : ",find)

#code to use replace method 
original_name=name.replace(name,original_name)
print("use of original name is : ",original_name)