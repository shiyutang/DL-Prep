import itertools

class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'

        for i in range(n-1):
        	result = ''.join([str(len(list(group)))+str(digit) for digit, group in itertools.groupby(result)])

        return result
sol = Solution()
print(sol.countAndSay(9))