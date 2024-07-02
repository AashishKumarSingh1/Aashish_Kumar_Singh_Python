class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums:
                if nums.index(complement) != i:
                    return [i, nums.index(complement)]
        return []
solution=Solution()
nums=[2,3,7]
target=9
result = solution.twoSum(nums, target)
print(result)