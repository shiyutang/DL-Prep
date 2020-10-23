class Solution1:
    def __init__(self):
        self.memoi = {}

    def translateNum(self, num: int) -> int:
        if not num:
            return 1
        elif int(num) < 10:
            return 1
        else:
            num = str(num)
            if num in self.memoi:
                return self.memoi[num]
            if 10 <= int(num[:2]) <= 25:
                nbrsols = self.translateNum(num[1:]) + self.translateNum(num[2:])
            else:
                nbrsols = self.translateNum(num[1:])
            print(self.memoi)
            self.memoi[num] = nbrsols
            return nbrsols


class Solution:
    def translateNum(self, num: int) -> int:
        nums = list(str(num))
        if len(nums) == 1:
            return 1
        p, q, r = 1, 1, 1
        before = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if 10 <= int(before + cur) <= 25:
                r = p + q
                p = q
                q = r
            else:
                p = q
                q = r
            before = cur
            # print(p,q,r)
        return r


sol = Solution()
print(sol.translateNum(12258))
print(sol.translateNum(26))
print(sol.translateNum(18822))
print(sol.translateNum(419605557))  # 2
print(sol.translateNum(1212121212121211))  # 8 1597
