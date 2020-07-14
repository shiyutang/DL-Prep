class Solution:
    def search(self, nums, target):
        if target not in nums:
            return -1

        mediumIdx = len(nums) // 2
        medium = nums[mediumIdx]
        first = nums[0]
        # print('mediumIdx,medium,first', mediumIdx,medium,first)

        if target == medium:
            # print('step 0')
            return mediumIdx

        if target == first:
            print('step 1')
            return 0
        elif target > first:
            if target > medium > first:
                print('step 2')
                return self.search(nums[mediumIdx + 1:], target) + mediumIdx + 1
            else:
                print('step 6')
                return self.search(nums[1:mediumIdx], target) + 1
        else:
            if target < medium < first:
                print('step 3')
                return self.search(nums[1:mediumIdx], target) + 1
            else:
                print('step 4')
                return self.search(nums[mediumIdx + 1:], target) + 1 + mediumIdx


sol = Solution()
# result = sol.search([11,12,13,2,3,4,5,6,7,8],2)
# result = sol.search([4,5,6,7,0,1,2],0)
# result = sol.search([1,3,5],5)
result = sol.search([8, 9, 2, 3, 4], 9)
print(result)
