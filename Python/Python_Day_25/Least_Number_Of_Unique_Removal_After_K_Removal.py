from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        sorted_counts = sorted(count.items(), key=lambda x: x[1])
        
        for key, freq in sorted_counts:
            if k >= freq:
                k -= freq
                del count[key]
            else:
                break

        return len(count)

solution = Solution()
arr = [4, 3, 1, 1, 2, 2, 3, 4, 4]
k = 3
print(solution.findLeastNumOfUniqueInts(arr, k))
