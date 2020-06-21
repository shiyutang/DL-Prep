# -*- coding:utf-8 -*-
# method 1: 时间复杂度O(N), 空间复杂度O(N)
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        numset = set()
        for num in array:
            if num in numset:
                numset.remove(num)
            else:
                numset.add(num)
        return [numset.pop(), numset.pop()]


# Method 2: 时间复杂度O(N), 空间复杂度O(1)
# 链接：https://www.nowcoder.com/questionTerminal/e02fdb54d7524710a7d664d082bb7811?answerType=1&f=discussion
# 来源：牛客网
#
# 方法二：位运算
# 前提知识：
# 异或运算：如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。
#
# n^0 = n; n^n = 0; n^n^m = n^(n^m) 满***换律
# 所以，我们可以让数组中的每一个数异或一下，最后会得到一个结果ret，就是两个出现一次的数字的异或结果这个结果肯定是由两个不同数字异或而来，
# 因此我们找ret二进制中为1的位置i，因为1一定是由0, 1异或而来，因此要求得两个数中，一定有一个数的二进制中的第i个位置为1， 一个为0.
#
# 如何找到位置i？可用i = ret ^ (-ret)
# 因为计算机用补码存取二进制数，而负数的补码为反码+1，举个例子
# 假如ret = 1110 ， -ret = 0010 , 所以 i = 0010
# 所以，第 i 位位 1 的全部异或就是 num1，剩下的全部异或就是 num2 。
class Solution2:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        ret, num1, num2 = 0, 0, 0
        for num in array:
            ret = ret ^ num
        indicator = ret & (-ret)
        for num in array:
            if num & indicator:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num
        return [num1, num2]


# sol = Solution()
sol = Solution2()
print(sol.FindNumsAppearOnce([1, 1, 2, 2, 3, 3, 4, 5]))
