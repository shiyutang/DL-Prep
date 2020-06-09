from collections import Counter

# 分别计算这个数两边的累乘就可以获得结果
class Solution:
    def productExceptSelf(self, nums):
        nlen = len(nums)
        a = Counter(nums)
        if a[0] > 1:
            return [0] * nlen

        premul, sufmul = [1], [1]
        for i in range(1, nlen):
            premul.append(premul[-1] * nums[i - 1])  # 还可以通过直接计算减少append的 开销
        for i in range(nlen - 1, 0, -1):
            sufmul.insert(0, sufmul[0] * nums[i])
        # print('premul,sufmul', premul, sufmul)

        for i in range(nlen):
            premul[i] = premul[i] * sufmul[i]

        return premul


sol = Solution()
res = sol.productExceptSelf([1, 2, 3, 0, 2, 0, 4])
print(res)
