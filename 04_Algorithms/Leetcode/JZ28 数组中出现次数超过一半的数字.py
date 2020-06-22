# 思想就是：如果两个数不相等，就消去这两个数，最坏情况下，每次消去一个众数和一个非众数，那么如果存在众数，最后留下的数肯定是众数
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        pool = numbers[:]
        while len(pool) > 1 and len(set(pool)) > 1:
            number1 = pool.pop(0)
            number2 = pool.pop(0)
            if number1 == number2:
                pool.extend([number1, number2])

        if not pool:
            return 0

        common = pool[0]
        cnt = 0
        for num in numbers:
            if common == num:
                cnt += 1
        if cnt > len(numbers) // 2:
            return common
        else:
            return 0


# 并不需要实际地消去，只需要记录众数地个数即可，当个数等于0 切换到另一个可能的众数
class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        cnt = 0
        for i, num in enumerate(numbers):
            if cnt == 0:
                tmp = num
                cnt += 1
            else:
                if tmp == num:
                    cnt += 1
                else:
                    cnt -= 1
        cnt = 0
        for num in numbers:
            if num == tmp:
                cnt += 1
        if cnt > len(numbers) // 2:
            return tmp
        return 0


sol = Solution1()
print(sol.MoreThanHalfNum_Solution([1, 2, 2, 2, 2, 2, 2, 5, 6]))
print(sol.MoreThanHalfNum_Solution([4, 2, 1, 4, 2, 4]))
