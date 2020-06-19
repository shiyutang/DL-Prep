# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0 or m == 0:
            return -1
        people = [i for i in range(n)]
        idx = m
        for i in range(n - 1):
            nbrpeople = n - i
            popidx = idx % nbrpeople - 1  # 每次计算到要弹出的idx，弹出那个元素
            people.pop(popidx)
            # print(people, popidx)
            if popidx == -1:
                idx = m          # 如果等于最后一个就重新开始
            else:
                idx = popidx + 1 + m - 1  # 否则就在现在的位置后推 m 个（因为index需要 +1 来恢复计数，同时每次删除之后后一个元素会前移）
        return people[0]

# 链接：https://www.nowcoder.com/questionTerminal/f78a359491e64a50bce2d89cff857eb6?answerType=1&f=discussion
# 来源：牛客网
#
# 方法二：递归
# 假设f(n, m) 表示最终留下元素的序号。比如上例子中表示为:f(5,3) = 3
#
# 首先，长度为 n 的序列会先删除第 m % n 个元素，然后剩下一个长度为 n - 1 的序列。那么，我们可以递归地求解 f(n - 1, m)，
# 就可以知道对于剩下的 n - 1 个元素，最终会留下第几个元素，我们设答案为 x = f(n - 1, m)。
#
# 由于我们删除了第 m % n 个元素，将序列的长度变为 n - 1。当我们知道了 f(n - 1, m) 对应的答案 x 之后，我们也就可以知道，
# 长度为 n 的序列最后一个删除的元素，应当是从 m % n 开始数的第 x 个元素。因此有 f(n, m) = (m % n + x) % n = (m + x) % n。
#
# 当n等于1时，f(1,m) = 0
# 代码为：
#
# class Solution {
# public:
#     int f(int n, int m) {
#         if (n == 1) return 0;
#         int x = f(n-1, m);
#         return (x+m) % n;
#     }
#     int LastRemaining_Solution(int n, int m)
#     {
#         if (n <= 0) return -1;
#         return f(n,m);
#     }
# };


sol = Solution()
print(sol.LastRemaining_Solution(6, 3))
