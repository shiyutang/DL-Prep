class Solution:
    def wordPattern(self, pattern, str):
        cast = {}
        strL = str.split()
        Plength =len(pattern)
        Slength = len(strL)
        print(Plength)
        print(Slength)
        if Plength != Slength:
            return False
        for i in range(Plength):
            if cast.__contains__(pattern[i]):
                if cast[pattern[i]] != strL[i]:
                    return False
            else:
                if strL[i] in cast.values():
                    return False
                cast[pattern[i]]=strL[i]
            print(cast)
        return True

sol = Solution()
res = sol.wordPattern('abba','cat dog dog cat')
print(res)
res = sol.wordPattern('abba','cat dog fish cat')
print(res)