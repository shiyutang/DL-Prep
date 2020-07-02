# -*- coding:utf-8 -*-
import copy


# 排列就是每次选择一位放在前面，之后的继承
class Solution:
    def Permutation(self, ss):
        memoi = set()
        if not ss:
            return ''
        else:
            def helper(string, pt):
                if len(string) == pt + 1:
                    memoi.add(string)
                else:
                    helper(string, pt + 1)
                    for i in range(pt+1, len(string)):
                        tmp = copy.deepcopy(string)  # swap string
                        tmp = tmp[:pt] + tmp[i] + tmp[pt + 1:i] + tmp[pt] + tmp[i + 1:]

                        helper(tmp, pt + 1)

            helper(ss, pt=0)
            ret = list(memoi)
            ret.sort()
            return ret


sol = Solution()
print(sol.Permutation('abc'))
print(sol.Permutation(''))
print(sol.Permutation('aabc'))
print(sol.Permutation('a'))
