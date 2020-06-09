from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        tmp = Counter(nums)
        print(tmp)

        tmplist = []
        for key in tmp:
            tmplist.append((key, tmp[key]))
        tmplist.sort(key=lambda s: s[1], reverse= True)
        print(tmplist)

        ret = []
        for i in range(k):
            ret.append(tmplist[i][0])
        return ret


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    nums, k = [1, 1, 1, 2, 2, 3, 5], 2
    print(nums, end=' ')
    res = sol.topKFrequent(nums, k)
    print(' and the res is ', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 10)
                nums.append(num1)
            print(nums, end=' ')
            res = sol.topKFrequent(nums, 5)
            print(' and the res is ', res)


test(Solution, True)
