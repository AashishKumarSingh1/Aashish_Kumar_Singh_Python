string1=input("Enter the first string : ")
string2=input('Enter the second string : ')
print(string2)
print(string1)
string1=string1.lower()
string2=string2.lower()
print(sorted(string1))
print(sorted(string2))

if(sorted(string2)==sorted(string1)):
    print(f"The {string1} and {string2} are Anagram!")
else:
    print("These String are not Anagram!")




