# 找出哪一部分是有序数组，且当目标在有序数组中时在有序数组中二分查找
class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        high, low = len(nums) - 1, 0
        while high > low:
            mid = (high + low) // 2
            print('low,high,mid', low, high, mid)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if nums[mid] > target >= nums[0]: # 注意判断边界，在左边边界的时候还是要往左边移动
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        if nums[high] == target:
            return high

        return -1


sol = Solution()
# print(sol.search([4, 5, 7, 8, 9, 1, 2, 3], 7))
# print(sol.search([4, 5, 7, 8, 9, 1, 2, 3], 8))
# print(sol.search([4, 5, 7, 8, 9, 1, 2, 3], 4))
# print(sol.search([4, 5, 7, 8, 9, 1, 2, 3], 3))
print(sol.search([3], 3))
print(sol.search([4, 5, 7, 8, 1, 2, 3], 4))
print(sol.search([4, 5, 7, 8, 1, 2, 3], 5))
# print(sol.search([4, 5, 7, 8, 9, 1, 2, 3], 6))
