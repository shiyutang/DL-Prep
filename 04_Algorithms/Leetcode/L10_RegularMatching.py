import re


class Solution:
    def isMatch(self, s, p):
        if s == p:
            return True
        PLen, SLen = len(p), len(s)
        countStar = len(re.findall("\*", p))
        if not (PLen == SLen) and (not ("*" in p) or not PLen - 2 * countStar <= SLen):
            return False
        else:
            equal = (s[0] == p[0]) or (p[0] == ".")
            if not equal and p[1] != "*":
                return False
            elif not equal and p[1] == "*":
                return self.isMatch(s[1:], p[2:])
            elif equal and p[0:2] == ".*":
                return self.isMatch(s[1:], p[1:])


sol = Solution()
s = "mississippi"
p = "mis*is*p*."
print(sol.isMatch(s, p))
s = "aab"
p = "c*a*b"
print(sol.isMatch(s, p))
print(sol.isMatch(s, p))
print(sol.isMatch(s, p))
print(sol.isMatch(s, p))
