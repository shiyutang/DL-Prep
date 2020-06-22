# -*- coding:utf-8 -*-
# 链接：https://www.nowcoder.com/questionTerminal/22243d016f6b47f2a6928b4313c85387?answerType=1&f=discussion
# 来源：牛客网
#
# 方法二：继续优化 空间复杂度O（1）时间复杂度O（N）
# 对于方法一中的：f[n] = f[n-1] + f[n-2] + ... + f[0]
#
# 那么f[n-1] 为多少呢？
#
# f[n-1] = f[n-2] + f[n-3] + ... + f[0]
#
# 所以一合并，f[n] = 2*f[n-1]，初始条件f[0] = f[1] = 1
#
# 所以可以采用递归，记忆化递归，动态规划，递推。具体详细过程，可查看青蛙跳台阶。
#
# 这里直接贴出递推的代码。

class Solution:
    def __init__(self):
        self.memoi = {1: 1, 2: 2}

    def jumpFloorII(self, number):
        if number < 1:
            return 0
        elif number in self.memoi:
            return self.memoi[number]
        else:
            res = 0
            for i in range(1, number):
                res += self.jumpFloorII(number - i)
            res += 1              # 一次跳n阶台阶
            self.memoi[number] = res
        return res


sol = Solution()
print(sol.jumpFloorII(3))
