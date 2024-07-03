import sys
class Solution:
    def dataTypeSize(self, type_str):
        if type_str == 'Character':
            return 1
        elif type_str == 'Integer':
            return 4 
        elif type_str == 'Float':
            return 4
        elif type_str == 'Long':
            return 8  
        elif type_str == 'Double':
            return 8 
        else:
            return -1  
        
        # size_bytes=sys.getsizeof(str)
        # return size_bytes
if __name__=='__main__':
    ob=Solution()
    res=ob.dataTypeSize(str(input("Enter the character : ")))
    print(res)
