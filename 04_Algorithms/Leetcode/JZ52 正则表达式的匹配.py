# -*- coding:utf-8 -*-
# pattern 中出现letter/./*。
# 仅当出现*的时候由于其可以匹配任意个前面的字符，
# 因此我们可以保持模式不变（继续匹配后面）/模式向后移动两位（*当成是匹配一位）
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # print(s,pattern)
        if not s and not pattern:  # 同时没有了就匹配上了
            return True
        elif not pattern:  # 只有pattern 没有
            return False
        else:  # s没有 或者都有
            if len(pattern) > 1 and pattern[1] == '*':  # 碰上了x*, 则可以匹配它也可以不匹配它
                if s and (s[0] == pattern[0] or pattern[0] == '.'):  # 有s且匹配，则可以匹配
                    return self.match(s[1:], pattern) or self.match(s[1:], pattern[2:]) or self.match(s, pattern[2:])
                else:  # 没有s 或者不匹配，就跳过
                    return self.match(s, pattern[2:])
            else:  # 没有碰上x*，则整除匹配
                if s and (s[0] == pattern[0] or pattern[0] == '.'):
                    return self.match(s[1:], pattern[1:])
            return False


sol = Solution()
# print(sol.match('abcd', 'ab*cd'))
# print(sol.match('abcd', ''))
# print(sol.match('aaaa', 'a*'))
# print(sol.match("", ".*"))
print(sol.match("bbbba", ".*a*a"))
# print(sol.match("a", "a*a"))
