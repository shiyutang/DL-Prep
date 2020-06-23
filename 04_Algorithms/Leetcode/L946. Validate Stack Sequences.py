class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        idx = 0
        while pushed:
            popval = popped[idx]
            if idx == 0:
                pointer = pushed.index(popval)
                pushed.pop(pointer)
                print(idx, popval, pushed, popped)
            else:
                tmpidx = pushed.index(popval)
                if tmpidx >= pointer -1:
                    pointer = tmpidx
                    pushed.pop(pointer)
                    print(idx, popval, pushed, popped)
                else:
                    return False
            idx += 1
        return True


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    # data = [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]
    # data = [1, 2, 3, 4, 5], [4, 3, 2, 1, 5]
    data = [1, 2, 3, 4, 5], [4, 5, 3, 1, 2]
    data = [0, 1, 2, 3, 5, 4], [3, 2, 1, 0, 4, 5]
    data = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
    data = [1], [4]
    # data = [2, 1, 3, 0], [1, 0, 3, 2]
    res = sol.validateStackSequences(data[0], data[1])
    print(res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 3)
                nums.append(num1)
            print('the nums are', nums)
            res = sol.hasGroupsSizeX(data)
            print(res)


test(Solution, False)
