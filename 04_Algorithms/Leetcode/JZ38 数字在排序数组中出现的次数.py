# -*- coding:utf-8 -*-
class Solution1:
    def GetNumberOfK(self, data, k):
        cnt = 0
        for i in data:
            if i == k:
                cnt += 1
            elif i > k:
                break
        return cnt


# 也可以通过二分查找，找到结果，并确定上界和下界
class Solution:
    def GetNumberOfK(self, data, k):
        low, high = 0, len(data) - 1
        while low < high:
            mid = (high + low) // 2
            if data[mid] < k:
                low = mid + 1 # 注意更新 low 和 high 的方式，保证其可以退出循环
            elif data[mid] == k:
                for lowbound in range(mid - 1, -1, -1):
                    if data[lowbound] != k:
                        break
                for highbound in range(mid + 1, len(data), 1):
                    if data[highbound] != k:
                        break
                # print(lowbound, highbound)
                res = highbound - lowbound - 2 + 1
                if lowbound == 0:        # 考虑自动结束循环的情况
                    res += 1
                if highbound == len(data) - 1:
                    res += 1
                return res
            else:
                high = mid - 1
            # print(low, high, mid)
        if data and data[low] == k:   # 考虑没有进入循环的情况以及输入为空的情况
            return 1
        else:
            return 0


sol = Solution()
print(sol.GetNumberOfK([1, 2, 4, 5, 7, 8, 8, 8, 8, 8], 8))
print(sol.GetNumberOfK([8], 8))
