# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        if not s:
            return ""
        slist = s.split(' ')
        res = ''
        for idx, item in enumerate(slist[::-1]):
            res += item
            if idx < len(slist)-1:
                res +=' '

        return res

sol = Solution()
print(sol.ReverseSentence('student. am I'))
print(sol.ReverseSentence("I am a student."))