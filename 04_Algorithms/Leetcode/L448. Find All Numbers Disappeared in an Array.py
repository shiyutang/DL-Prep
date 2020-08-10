# 每次对于每个数字进行交换，换到它索引所在的位置，没有可换的就设置为0
# 官方题解：不需要交换，碰到对应索引的就标注为负数，已经是负数的不再标注，最后看那些位置是正数就是没出现过的
class Solution:
    def findDisappearedNumbers(self, nums):
        i = 0
        while i < len(nums):
            num1 = nums[i]
            num2 = nums[num1 - 1]

            if num1 == 0 or num1 == i + 1:
                i += 1
                continue

            if not num2 or num1 == num2:
                nums[i] = 0
                nums[num1 - 1] = num1
            else:
                nums[i], nums[num1 - 1] = num2, num1
            # print(nums)
        ret = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ret.append(i + 1)
        return ret


sol = Solution()
print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(sol.findDisappearedNumbers([1, 1]))
print(sol.findDisappearedNumbers([2, 2]))
