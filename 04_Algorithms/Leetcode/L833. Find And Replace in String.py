class Solution:
    def findReplaceString(self, S: str, indexes, sources, targets) -> str:
        # 找到确实匹配且需要替换的
        valididxsource = []
        for i, ele in enumerate(indexes):
            if S[ele:ele + len(sources[i])] == sources[i]:
                valididxsource.append((ele, sources[i], targets[i]))

        valididxsource.sort(key=lambda s: s[0])
        print(valididxsource)

        # concate
        previd = 0
        ret = ''
        for idx, source, target in valididxsource:
            print(ret, previd)
            ret += S[previd:idx] + target
            previd = idx + len(source)
        ret += S[previd:]

        return ret


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    # data = "abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]
    # data = "abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]
    data = "", [1, 3, 4], ["a", "c", "sa"], ["eee", "ffff", 'qqqq']
    res = sol.findReplaceString(data[0], data[1], data[2], data[3])
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
