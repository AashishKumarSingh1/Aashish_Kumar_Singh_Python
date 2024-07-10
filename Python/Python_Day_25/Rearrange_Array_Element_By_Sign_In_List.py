class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        rea_list=[None]*len(nums)
        even_counter=0
        odd_counter=1
        for num in nums:
            if num>=0:
                rea_list[even_counter]=num 
                even_counter+=2
            else:
                rea_list[odd_counter]=num
                odd_counter+=2
        return rea_list