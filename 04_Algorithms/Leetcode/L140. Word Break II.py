class Solution:
    def wordBreak(self, s: str, wordDict):
        if not s:
            return []

        ret = []
        memoi = set()

        def helper(string, buf):
            if not string:
                ret.append(''.join(buf).strip())
                return True
            if string in memoi:
                return False
            flag = False
            for phrase in wordDict:
                if string[:len(phrase)] == phrase:
                    tmp = buf[:] + [phrase + ' ']
                    res = helper(string[len(phrase):], tmp)
                    flag = any([flag, res])
                    if not res:
                        memoi.add(string)
            return flag

        helper(s, [])
        return ret


sol = Solution()
# print(sol.wordBreak("catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
# print(sol.wordBreak("pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
# print(sol.wordBreak("catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
