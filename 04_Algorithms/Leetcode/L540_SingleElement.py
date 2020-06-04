class Solution(object):
    def singleNonDuplicate(self, nums):
        res = None
        if not nums:
            return 0
        while res==None:
            center = int(len(nums)/2)
            if center%2 == 1:
                center += 1
            # print(center)
            if center+1>=len(nums):
                if nums[center] == nums[center - 1]:
                    res = nums[0]
                else:
                    res = nums[center]
            elif center-1<0:
                if nums[center] == nums[center + 1]:
                    res = nums[-1]
                else:
                    res = nums[0]
            else:
                if nums[center] == nums[center + 1]:
                    nums = nums[center:]
                    continue
                elif nums[center] == nums[center-1]:
                    nums = nums[:center+1]
                    continue
                elif nums[center]!=nums[center+1] and nums[center] != nums[center-1]:
                    res = nums[center]
        # print(res)
        return res

sol = Solution()
# sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
# sol.singleNonDuplicate([3,3,7,7,10,11,11])
# sol.singleNonDuplicate([3,10,10])
sol.singleNonDuplicate([0,1,1])

