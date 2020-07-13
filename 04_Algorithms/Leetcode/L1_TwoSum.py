# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# O(N) O(N) 利用字典找另外一个数
class Solution:  # infor: only two nums add together
    def twoSum(self, nums, target):
        num2indices = {}

        for k, num in enumerate(nums):
            remain = target - num
            if remain in num2indices and num2indices[remain] != k:
                return [k, num2indices[remain]]

            num2indices[num] = k

        return []


# 排序+ 双指针，O(N), O(1)


sol = Solution()
res = sol.twoSum(nums=[2, 3, 7, 8, 11, 15], target=15)
res = sol.twoSum(nums=[2, 3, 1, 8, 11, 15], target=15)
res = sol.twoSum(nums=[0, 4, 3], target=0)
print(res)
