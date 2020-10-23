# 注意到C中方块求和，实际上是 A,B 不同情况累计和的乘积，因此求出A,B最大最小累积和相乘即可
# 2 3 4 -4 -3 3 2 -30 10 10
# class Solution {
# public:
#     int maxSubArray(vector<int>& nums) {
#         int pre = 0, maxAns = nums[0];
#         for (const auto &x: nums) {
#             pre = max(pre + x, x);
#             maxAns = max(maxAns, pre);
#         }
#         return maxAns;
#     }
# };

class Solution:
    def maxsum(self, array: list, minus=False) -> int:
        maxsum = [array[0],-1*array[0]][minus]
        pre = 0
        for ele in array:
            if minus:
                ele = -1 * ele
            pre = max(pre + ele, ele)
            maxsum = max(maxsum, pre)

        return maxsum

    def solve(self, A, B):
        maxA = self.maxsum(A)
        minA = -1 * self.maxsum(A, minus=True)
        maxB = self.maxsum(B)
        minB = -1 * self.maxsum(B, minus=True)
        return max([maxA * maxB, maxA * minB, minA * maxB, minA * minB])


N, M = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
sol = Solution()
print(sol.solve(A, B))
