from collections import Counter


class Solution:
    def minDominoRotations(self, A: list, B: list) -> int:
        ACounter = Counter(A)
        BCounter = Counter(B)

        def util(counter, ID, freq, val, tag):
            for ele in counter:
                if counter[ele] > freq:
                    ID = tag
                    freq = counter[ele]
                    val = ele

            return ID, freq, val

        AID, Afreq, Aval = util(ACounter, "A", -1, -1, 'A')
        BID, Bfreq, Bval = util(BCounter, "A", Afreq, Aval, 'B')
        notChoseID = ["A", "B"][BID == "A"]
        # print(notChoseID, BID, Bfreq, Bval)
        if Bfreq < len(A)//2:
            return -1

        cnt = 0
        for idx, ele in enumerate(eval(BID)):
            if ele is not Bval:
                if eval(notChoseID)[idx] != Bval:
                    return -1
                else:
                    cnt += 1
            # print(idx, ele, Bval, cnt)
        return cnt

# 第一对任选一个，一定要存在在后面的
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in (A[0], B[0]):
            if all(x in pair for pair in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))

        return -1

def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    # data = [2, 4, 2, 4, 4, 2], [4, 2, 4, 2, 2, 4]
    # data = [3, 5, 1, 2, 3], [3, 6, 3, 3, 4]
    data = [1,0], [0,1]
    res = sol.minDominoRotations(data[0], data[1])
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
