import numpy as np


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text2 is '' or text1 is '':
            return 0
        LCS = np.zeros((len(text1) + 1, len(text2) + 1))
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    LCS[i, j] = LCS[i - 1, j - 1] + 1
                else:
                    LCS[i, j] = max(LCS[i - 1, j], LCS[i, j - 1])

        return int(LCS[len(text1), len(text2)])


# test
import random
import string

# test settings
times = 100

sol = Solution()

for _ in range(times):
    len1, len2 = random.randint(0, 10), random.randint(1, 10)
    str1 = ''.join(random.sample(string.ascii_lowercase, len1))
    str2 = ''.join(random.sample(string.ascii_lowercase, len2))
    print(str1, str2, end=' ')
    res = sol.longestCommonSubsequence(str1, str2)
    print(' and their LCS is ', res)
