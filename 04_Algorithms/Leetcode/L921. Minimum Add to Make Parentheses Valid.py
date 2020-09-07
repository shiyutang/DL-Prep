# 左括号前有右括号
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        leftcnt, rightcnt = 0, 0
        for ele in S:
            if ele == '(':
                leftcnt += 1
            else:
                if leftcnt != 0:
                    leftcnt -= 1
                else:
                    rightcnt += 1
        return leftcnt + rightcnt


sol = Solution()
print(sol.minAddToMakeValid('())'))
print(sol.minAddToMakeValid(''))
print(sol.minAddToMakeValid('()))(('))
print(sol.minAddToMakeValid('()'))
print(sol.minAddToMakeValid('(())'))
print(sol.minAddToMakeValid('(()))('))
