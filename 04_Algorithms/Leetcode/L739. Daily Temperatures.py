# 单调栈 O（n）时间获得结果并放到给定结果中
class Solution:
    def dailyTemperatures(self, T):
        stack = []  # 从左到右逐渐递减是找最大
        record = [0] * len(T)

        for idx, ele in enumerate(T):
            if stack:
                while stack and ele > T[stack[-1]]:
                    record[stack[-1]] = idx-stack[-1]
                    stack.pop(-1)
            stack.append(idx)
            # print('stack,record,ele,idx', stack, record, ele, idx)

        return record


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    a = [3, 7, 0, 9, 6, 5, 8, 4, 1, 2]
    a = [0]

    res = sol.dailyTemperatures(a)
    print(' and the res is ', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(0, 20)
                nums.append(num1)
            print('the inputs are', nums)
            res = sol.dailyTemperatures(nums)
            print(' and the res is ', res)


test(Solution, True)
