# -*- coding:utf-8 -*-
# 根据pop的顺序确定第一个压入栈的元素，之后我们不能直接pop在其之前压入的元素

class Solution:
    def IsPopOrder(self, pushV, popV): # 还有可能pop和push中元素不相等的情况
        if set(pushV) != set(popV):
            return False

        pre = -1
        while popV:
            val = popV.pop(0)
            idx = pushV.index(val)
            if pre == -1:
                pre = idx
                pushV.pop(idx)
            else:
                if idx < pre - 1:
                    return False
                else:
                    pre = idx
                    pushV.pop(idx)
        return True


def test(method, random_samples=False):
    sol = method()
    # data = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]
    # data = [1, 2, 3, 4, 5], [4, 3, 2, 1, 5]
    data = [1, 2, 3, 4, 5], [4, 5, 3, 1, 2]
    data = [0, 1, 2, 3, 5, 4], [3, 2, 1, 0, 4, 5]
    data = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
    # data = [2, 1, 3, 0], [1, 0, 3, 2]
    res = sol.IsPopOrder(data[0], data[1])
    print(res)


test(Solution, False)
