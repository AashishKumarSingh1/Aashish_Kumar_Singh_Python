import math
class Solution:
    def switchCase(self, choice, arr):
        if choice==1:
            r=arr[0]
            return math.pi*r*r
        elif choice==2:
            concatenated_str = ''.join(map(str, arr))
            combined_int = int(concatenated_str)
            l = combined_int // 10  
            b = combined_int % 10 
            # l,b=arr[0],arr[1]
            return l*b
object1=Solution()
area_c=object1.switchCase(1,[8])
area_r=object1.switchCase(2,[2, 3])
print(area_c,'\n',area_r)
