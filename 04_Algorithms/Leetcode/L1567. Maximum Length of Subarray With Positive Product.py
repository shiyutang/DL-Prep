class Solution:
    def getMaxLen(self, inputnums: list) -> int:

        return max(self.getMaxLenhelper(inputnums), self.getMaxLenhelper(inputnums[::-1]))

    def getMaxLenhelper(self, nums: list) -> int:
        cnt, ret = 0, 0
        minus, zeros = None, None
        for i, ele in enumerate(nums):
            if ele > 0:
                if minus is None:
                    cnt += 1
            elif ele == 0:
                if minus is None:
                    ret = max(ret, cnt)
                else:
                    ret = max([ret, cnt, i - minus - 1])
                    minus = None
                cnt = 0
                zeros = i
            else:
                if minus is not None:
                    cnt += i - minus + 1
                    minus = None
                else:
                    minus = i
            # print('minus, cnt, ret, ele, i', minus, cnt, ret, ele, i)
        else:
            if minus is not None and zeros is not None:
                lastpiece = len(nums) - 1 - max(minus, zeros)
            elif zeros is not None:
                lastpiece = len(nums) - 1 - zeros
            elif minus is not None:
                lastpiece = len(nums) - 1 - minus
            else:
                lastpiece = 0
            ret = max([ret, lastpiece, cnt])
        return ret


sol = Solution()
# print(sol.getMaxLen([1, 2, 3, 0, 2, 3, 2, -1, 3, 4, 3, 5, 2]))
# print(sol.getMaxLen([1, 2, 3, 0, 2, 3, 2, -1, 3, 4, -3, 5, 2]))
# print(sol.getMaxLen([1, 2, 3, 0, 2, 3, 2, -1, 3, 4, 0, 5, 2]))
# print(sol.getMaxLen([1, 2, 3, 0, 2, 3, 2, -1, 3, 4, 0, 5, -5]))
# print(sol.getMaxLen([1, 2, 3]))
# print(sol.getMaxLen([-1, -2, 3]))
# print(sol.getMaxLen([1, -2, -3]))
# print(sol.getMaxLen([1, 0, -3]))
# print(sol.getMaxLen([-1, 0, -3]))
# print(sol.getMaxLen([1, -2, -3, 4]))
# print(sol.getMaxLen([1]))
# print(sol.getMaxLen([]))
# print(sol.getMaxLen([0, 1, -2, -3, -4]))
# print(sol.getMaxLen([-1, -2, -3, 0, 1]))
# print(sol.getMaxLen([-1, 2]))
print(sol.getMaxLen([5, -20, -20, -39, -5, 0, 0, 0, 36, -32, 0, -7, -10, -7, 21, 20, -12, -34, 26, 2]))
# print(sol.getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]))
