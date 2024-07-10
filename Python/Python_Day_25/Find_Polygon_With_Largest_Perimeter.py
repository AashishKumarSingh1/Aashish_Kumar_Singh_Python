class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        count=len(nums)
        nums.sort()
        while count>=3 and nums!=[]:
            max_value=max(nums)
            sum_num=sum(nums)-max_value

            if max_value<sum_num:
                return sum(nums)
            else:
                # nums.pop()
                # def nums[-1]
                nums.remove(max(nums))
                continue

            count-=1
        return -1

            

        