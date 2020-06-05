class Solution:
    def maximumSwap(self, num: int) -> int:
        numlist = list(str(num))
        numLen = len(numlist)

        cmp = numlist[:]
        cmp.sort(reverse=True)  # str can sort like numbers

        # find the first different val is the one need to be swapped
        for i in range(numLen):
            if cmp[i] != numlist[i]:
                swapval = cmp[i]
                break
            if i == numLen - 1:  # nothing to swap
                return int(num)

        for j in range(numLen-1, i, -1):
            if numlist[j] == swapval:
                break

        numlist[i], numlist[j] = numlist[j], numlist[i]
        return int(''.join(numlist))


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()

    res = sol.maximumSwap(num=33213319)
    print(' and the swap res is ', res)
    res = sol.maximumSwap(num=0)
    print(' and the swap res is ', res)

    if random_samples:
        import random

        for _ in range(times):
            nums = random.randint(0, 1e8)
            print('the nums is', nums)
            res = sol.maximumSwap(nums)
            print(' and the swap res is ', res)


test(Solution, True)
