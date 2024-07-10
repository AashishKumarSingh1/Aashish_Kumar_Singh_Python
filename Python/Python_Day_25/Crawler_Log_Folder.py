from typing import List
#Stack Based Algorithm
class Solution:
    def minOperations(self,logs: List[str]) -> int:
        return self.create_file(logs)

    @staticmethod
    def create_file(logs: List[str]) -> int:
        stack = []
        for folder in logs:
            if folder == './':
                continue
            elif folder == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        return len(stack)
    
Solution1=Solution()
print(Solution1.minOperations(["d1/","d2/","../","d21/","./"]))

