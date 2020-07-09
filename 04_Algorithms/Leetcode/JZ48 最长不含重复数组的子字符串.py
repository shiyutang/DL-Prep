# 使用一个指针 prev 记录在这个指针之后就没有重复的部分，
# 仅当有重复字符而且重复的在 prev 的部分时更新指针
# 最后记录数组中最多不重复的部分返回
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = -1   # set margin right could save a lot of trouble, think about its meaning
        ret = 0
        letters = dict()
        for i, letter in enumerate(s):
            if letter in letters and prev < letters[letter]:
                prev = letters[letter]
            letters[letter] = i

            ret = max(ret, i - prev)  # update ret based on the prev

        return ret


sol = Solution()
print(sol.lengthOfLongestSubstring('abcdcab'))
print(sol.lengthOfLongestSubstring(''))
print(sol.lengthOfLongestSubstring("tmmzuxt"))
print(sol.lengthOfLongestSubstring('abcdabcd'))
print(sol.lengthOfLongestSubstring('abcdcabdab'))
print(sol.lengthOfLongestSubstring("abfdshfkaksfbcakhsoaihabfeoifnanfslacnlanceoonczsccabcbb"))
