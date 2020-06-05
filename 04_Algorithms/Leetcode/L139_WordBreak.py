class Solution:
    def __init__(self):
        self.memoi = []  # recursive problem remember to save calculated result in a memoi to save A LOT OF time

    def wordBreak(self, s: str, wordDict) -> bool:
        if s is '':
            return True
        elif s in self.memoi:
            return False

        for word in wordDict:
            if s.startswith(word):
                out = self.wordBreak(s[len(word):], wordDict)
                if out:
                    return True
                else:
                    self.memoi.append(s)
        return False


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    res = sol.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        , ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
    print(res)
    res = sol.wordBreak("leetcode", ["leet", "code"])
    print(res)
    res = sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print(res)
    res = sol.wordBreak("bb", ["a", "b", "bbb", "bbbb"])
    print(res)
    res = sol.wordBreak("cars", ["car", "ca", "rs"])
    print(res)


test(Solution, True)
