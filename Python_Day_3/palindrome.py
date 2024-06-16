""""
This program is going to print the palindrome number
Palindrome number : the number or string that sounds same from front or from behind

"""

str = str(input("Enter the number or string: "))
# rev_str= str.__reversed__ => this is a wrong method to print the reverse of a string
rev_str = str[::-1] # => this is a right method to print the reverse of a string 

# reversed_string = ''.join(reversed(user_string)) # => this is a right method to print the reverse of a string
if (str==rev_str):
    print(str, " is a Palindrome Number!")

else:
    print(str, " is not a Palindrome number!")