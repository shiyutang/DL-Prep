from collections import defaultdict

# ！！ 需要特定元素之间连接成功，而不是相同长度有连接就可以， 代码需要修改
# noinspection SpellCheckingInspection
class Solution:
    def longestStrChain(self, words: list) -> int:
        # 1. 长度字典，筛选出最长的连续长度
        if len(words) < 2:
            return len(words)
        lenDict = defaultdict(list)
        lenList = []
        for word in words:
            wordLen = len(word)
            lenDict[wordLen].append(word)
            if wordLen not in lenList:
                lenList.append(wordLen)
        lenList.sort()
        print(lenList, lenDict)

        # 2. 对于所有长度，判断长度连结，有连结加1，没有则清零，记录最大返回
        def connect(smallstr, bigstr):
            l1, l2 = len(smallstr), len(bigstr)
            i = j = 0
            while i < l1 and j < l2:
                if smallstr[i] == bigstr[j]:
                    i, j = i + 1, j + 1
                else:
                    j += 1
                if j > i + 1:
                    return False
            return True

        def connectgrp(smallgrp, biggrp):
            for ele in smallgrp:
                for cmp in biggrp:
                    if connect(ele, cmp):
                        return True
            return False

        maxLen, length = 0, 0
        for idx, ele in enumerate(lenList[:-1]):
            len1, len2 = lenList[idx], lenList[idx + 1]
            if len1 == len2 - 1 and connectgrp(lenDict[len1], lenDict[len2]):
                length += 1
            else:
                maxLen = max(maxLen, length)
                length = 0
            print(length, lenList[idx], lenList[idx + 1], lenDict[len1], lenDict[len2])

        return max(maxLen, length) + 1


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = ["a", "b", "ba", "bca", "bda", "bdca"]
    data = ["a", "ba", "bec", "bea", "bdca", "bddda"]
    data = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
            "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
    res = sol.longestStrChain(data)
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
