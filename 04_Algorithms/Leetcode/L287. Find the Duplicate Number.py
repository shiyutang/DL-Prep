# class Solution:
# 	def findDuplicate(self, nums) -> int:
# 		t, h = nums[0], nums[nums[0]]
#
# 		while t != h:
# 			print(t, h)
# 			t, h = nums[t], nums[nums[h]]
#
# 		t = 0
# 		while t != h:
# 			print('t,h', t, h)
# 			t, h = nums[t], nums[h]
#
# 		print(t)
# 		return t
#


class Solution:
    def findDuplicate(self, nums):
        n = len(nums) - 1
        high, low = n, 1

        while high > low:
            middle = (high + low) / 2
            print('low,high,middle', low, high, middle)
            small, big, mid = 0, 0, 0
            for ele in nums:
                if low <= ele < middle:    # 使用二分法时，每次只需要比较low和high之间的数字
                    small += 1
                elif high >= ele > middle:
                    big += 1
                elif ele == middle:        # 考虑正好相等
                    mid += 1
            print('small, big', small, big)
            if small == big or mid > 1:
                return int(middle)
            elif small > big:
                high = [int(middle) - 1, int(middle)][int(middle) != middle]  # 另外在更新middle时需要注意奇偶长度的往上和往下更新不同，
            else:
                low = int(middle) + 1
        return high


sol = Solution()
res = sol.findDuplicate([1, 2, 3, 4, 2, 5])
# res = sol.findDuplicate([2, 2, 2, 2, 2, 2, 1])
# res = sol.findDuplicate([1, 3, 4, 2, 2, 5, 6, 7, 9, 8])
# res = sol.findDuplicate([1, 3, 4, 2, 8, 5, 6, 7, 9, 8])
# res = sol.findDuplicate([1, 3, 4, 2, 9, 5, 6, 7, 9, 8])
# res = sol.findDuplicate([1, 3, 4, 2, 1])

print(res)
