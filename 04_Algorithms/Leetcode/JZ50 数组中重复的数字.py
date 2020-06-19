# -*- coding:utf-8 -*-
# 链接：https://www.nowcoder.com/questionTerminal/623a5ac0ea5b4e5f95552655361ae0a8?answerType=1&f=discussion 来源：牛客网
# 方法二：in-place算法
# 方法一中的一个条件我们没有用到。也就是数据的范围是0-n-1。所以我们可以这么做：
#
# 设置一个指针i指向开头0，
#
# 对于arr[i]进行判断，如果arr[i] == i， 说明下标为i的数据正确的放在了该位置上，让i++
#
# 如果arr[i] != i, 说明没有正确放在位置上，那么我们就把arr[i]放在正确的位置上，也就是交换
# arr[i] 和arr[arr[i]]。交换之后，如果arr[i] ！= i, 继续交换。
#
# 如果交换的过程中，arr[i] == arr[arr[i]]，说明遇到了重复值，返回即可。

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        numset = set()
        for num in numbers:
            if num in numset:
                duplication[0] = num
                return True
            else:
                numset.add(num)
        return False