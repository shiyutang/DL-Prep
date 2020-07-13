class Solution:
    def threeSum(self, nums):
        nums.sort()
        ret = []
        for i in range(len(nums) - 1):
            first = nums[i]
            if i - 1 >= 0 and first == nums[i - 1]:
                continue
            target = 0 - first
            pt1, pt2 = i + 1, len(nums) - 1
            while pt1 < pt2:
                remain = target - nums[pt1]
                if remain > nums[pt2]:
                    pt1 += 1
                elif remain == nums[pt2]:
                    second = nums[pt1]
                    ret.append([first, second, remain])
                    pt1 += 1
                    pt2 -= 1
                    while pt1 < pt2 and nums[pt1] == second:
                        pt1 += 1
                    while pt1 < pt2 and nums[pt2] == remain:
                        pt2 -= 1
                else:
                    pt2 -= 1
        return ret


sol = Solution()
print(sol.threeSum([0, 0, 0, 0, 0, 0, 0, 0]))
print(sol.threeSum([0, 0]))
print(sol.threeSum([1, -1, 1]))
print(sol.threeSum([1, -1, 0, -1, 0, 1]))
