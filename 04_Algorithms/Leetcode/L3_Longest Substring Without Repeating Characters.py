class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        shownLetter = []
        maxlen = 0
        for i in range(len(s)):
            if not s[i] in shownLetter:
                shownLetter.append(s[i])
                length+=1
            elif s[i] == shownLetter[0]:
                shownLetter.pop(0)
                shownLetter.append(s[i])
            else:
                idx = shownLetter.index(s[i])  #重复字母所在位置
                shownLetter = shownLetter[idx+1:]
                shownLetter.append(s[i])
                if length>maxlen:
                    maxlen = length
                length = len(shownLetter)
            # print(shownLetter)
            # print(length)
            # print(maxlen)
        return max(maxlen,length)

sol = Solution()
res = sol.lengthOfLongestSubstring("abcabcbb")
print(res)
res = sol.lengthOfLongestSubstring("pwwkew")
print(res)
res = sol.lengthOfLongestSubstring("bbbbbbb")
print(res)
res = sol.lengthOfLongestSubstring("abcdabcfsaehfoifhalfhoirioaoihfklvnkhxdodhoiefknk")
print(res)

