class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n<m:
            return 'lesser'
        elif n==m:
            return 'equal'
        elif n>m:
            return 'greater'
        else:
            pass
object_1=Solution()
compare=object_1.compareNM(int(input("Enter the first number : ")),int(input("Enter the second number : ")))
print("Result is : ", compare)