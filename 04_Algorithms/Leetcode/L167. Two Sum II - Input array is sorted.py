class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start,end = 0,len(nums)-1
        while nums[start]+nums[end] != target:
            if nums[start]+nums[end]>target:
                end -= 1
            else:
                start += 1
        return [start+1,end+1]