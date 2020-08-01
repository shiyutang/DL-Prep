class Solution:
    def partition(self, s: str):
        if not s:
            return [['']]

        ret = []
        dp = [[False for _ in range(len(s))] for __ in range(len(s))]

        print(dp)
        for step in range(0, len(s)):
            for i in range(len(s) - step):
                tmp = s[i:i + step+1]
                if len(tmp) == 1:
                    dp[i][i+step] = True
                else:
                    if tmp[-1] == tmp[0]:
                        if len(tmp) == 2:
                            dp[i][i+step] = True
                        else:
                            dp[i][i+step] = dp[i + 1][i+step - 1]

        def helper(start, buf):
            if start == len(s):
                ret.append(buf)
                return
            else:
                for jk in range(len(s) - start):
                    if dp[start][start + jk]:
                        tmp = buf[:]
                        tmp.append(s[start:start + jk + 1])

                        helper(start + jk + 1,  tmp)
                    else:
                        continue

        helper(0, [])

        return ret

class Solution1(object):
    # 本题采用回溯法
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 定义一列表，用来保存最终结果
        split_result = []
        # 如果给定字符串s为空，则没有分割的必要了
        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return
            for end in range(start+1, len(s)+1):
                split_s = s[start:end]
                # 如果当前子串为回文串，则可以继续递归
                if split_s == s[start:end][::-1]:
                    back(end, res+[split_s])

        back()
        return split_result

sol = Solution()
# print(sol.partition('ABACABA'))
print(sol.partition('abacaba'))
print(sol.partition('aab'))

sol = Solution1()
# print(sol.partition('ABACABA'))
print(sol.partition('abacaba'))
print(sol.partition('aab'))