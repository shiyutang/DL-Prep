import numpy as np


class Solution:
    def solve(self, n, a: list):
        mono_stack = []  # 由左往右不断递减
        record = {}
        for idx, item in enumerate(a):
            if not mono_stack:
                mono_stack.append((idx, item))
            else:
                i = len(mono_stack) - 1
                while i >= 0 and item > mono_stack[i][1]:
                    if i - 1 >= 0:
                        record[mono_stack[i][0]] = (mono_stack[i - 1][0], idx)
                    else:
                        record[mono_stack[i][0]] = (-1, idx)
                    mono_stack.pop(i)
                    i -= 1
                mono_stack.append((idx, item))
        while mono_stack:
            if len(mono_stack) >= 2:
                record[mono_stack[-1][0]] = (mono_stack[-2][0], -1)
            else:
                record[mono_stack[-1][0]] = (-1, -1)
            mono_stack.pop(-1)

        max_xor = -float('inf')
        for key in record:
            val = a[key]
            if a[record[key][0]] == -1 and a[record[key][1]] == -1:
                continue
            elif a[record[key][0]] == -1:
                max_a = a[record[key][1]]
            elif a[record[key][1]] == -1:
                max_a = a[record[key][0]]
            else:
                max_a = a[record[key][0]]
                xor_val = val ^ max_a
                max_xor = [max_xor, xor_val][xor_val > max_xor]

                max_a = a[record[key][1]]
            xor_val = val ^ max_a
            max_xor = [max_xor, xor_val][xor_val > max_xor]

        return max_xor


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    # n, a = 10, [3, 7, 0, 9, 6, 5, 8, 4, 1, 2]
    n, a = 5, [0, 7, 2, 5, 9]

    res = sol.solve(n, a)
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
            res = sol.solve(len1, nums)
            print(' and res', res)


test(Solution, True)
