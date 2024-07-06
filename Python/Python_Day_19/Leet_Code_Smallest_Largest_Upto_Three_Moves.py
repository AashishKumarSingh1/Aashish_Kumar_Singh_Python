import time
class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2 or len(nums)==3 or len(nums)==4:
            return 0 
        else:
            nums.sort()
            diff=max(nums)-min(nums)
            count=0
            while diff!=0 and count<=3:
                if count==len(nums)//2:
                    nums[-(count+1)] = min(nums)
                    continue
                nums[-(count+1)]=nums[count] 
                diff=max(nums)-min(nums)
                count+=1                
            return diff
object1=Solution()
time_start=time.time()
print(time_start)
result=object1.minDifference([3,100,20])
time_end=time.time()
print(result)
print('diff_time: ',(time_end-time_start))

        