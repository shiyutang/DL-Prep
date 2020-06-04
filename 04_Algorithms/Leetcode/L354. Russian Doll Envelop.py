import bisect

# if you sorted height, then it is no need to compare it
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if len(envelopes)==0 or len(envelopes) == 1:
            return len(envelopes)
        envelopes.sort(key=lambda s: (s[0], -s[1]))
        # sort the second dim in reverse order to replace with the smaller width when the height is the same
        # print('The sorted envelop is', envelopes)

        selectedEn = []
        widths = list(map(lambda s: s[1], envelopes))
        # print('The widths are ', widths)
        for i, width in enumerate(widths):
            idx = bisect.bisect_left(selectedEn, width)
            if idx >= len(selectedEn):
                selectedEn.append(width)
            else:
                selectedEn[idx] = width
            # print(selectedEn)

        return len(selectedEn)


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    nums = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print(nums, end=' ')
    res = sol.maxEnvelopes(nums)
    print(' and the max envelop is ', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1, num2 = random.randint(0, 100), random.randint(0, 100)
                nums.append([num1, num2])
            res = sol.maxEnvelopes(nums)
            print(' and the max envelop is ', res)


test(Solution, True)
