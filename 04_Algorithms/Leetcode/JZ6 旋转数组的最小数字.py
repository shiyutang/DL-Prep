# -*- coding:utf-8 -*-

# 懒方法看题目为什么不对
class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        ret = rotateArray[0]
        for num in rotateArray:
            ret = min(ret, num)
        return ret


# 二分查找中间的最小值
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        low, high = 0, len(rotateArray) - 1
        mid = (high + low) // 2
        ret = rotateArray[0]
        while low < high:
            if rotateArray[low] < rotateArray[high]:
                return rotateArray[low]
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            elif rotateArray[mid] > rotateArray[high]:
                high = mid
            else:
                high -= 1
            ret = min(ret, rotateArray[mid])

            mid = (high + low) // 2
        return ret


sol = Solution()
print(sol.minNumberInRotateArray([4, 5, 6, 3, 4]))
