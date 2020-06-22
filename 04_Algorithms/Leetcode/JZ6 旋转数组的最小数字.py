# -*- coding:utf-8 -*-
# 二分查找中间的最小值
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        low, high = 0, len(rotateArray) - 1
        mid = (high + low) // 2
        ret = rotateArray[0]
        while low < high:
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            else:
                ret = min(ret, rotateArray[mid])
                high = mid
            mid = (high + low) // 2
        return ret


sol = Solution()
print(sol.minNumberInRotateArray([4]))
