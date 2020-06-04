def KMPSearch(pat, txt):
    M, N = len(pat), len(txt)
    # create pi[] that will hold the longest prefix suffix values for pattern
    pi = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern ()
    computeLPSArray(pat, M, pi)  # calculate pi[] array

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            # print("Found pattern at index " + str(i - j))
            j = pi[j - 1]
            return i - j

            # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            if j != 0:  # 在匹配了部分字符串之后不匹配，那么，变换模式指向位置，使得其右移j-π[j]位
                j = pi[j - 1]
            else:  # 一个也没有匹配上,pattern移向下一位
                i += 1


def computeLPSArray(pat, M, pi):
    len = 0  # length of the previous longest prefix suffix

    pi[0] = 0  # pi[0] is always 0
    j = 1
    # the loop calculates pi[i] for i = 1 to M-1
    while j < M:
        if pat[j] == pat[len]:
            len += 1
            pi[j] = len
            j += 1
        else:
            if len != 0:
                len = pi[len - 1]
            else:
                pi[j] = 0
                j += 1


import  copy
class Solution:
    def findSubstring(self, s, words):
        if s =='' or words == []:
            return []
        slength = len(s)
        wlength = len(words[0])
        for word in words:
            if len(word) != wlength:
                return []
        if slength < wlength*len(words):
            return []
        wordsidx = []
        for word in words:
            string = copy.deepcopy(s)
            removeidx = 0
            while KMPSearch(word,string):
                wordidx = KMPSearch(word,string)
                wordsidx.append(wordidx-wlength+removeidx)
                string = string[(wordidx):]
                removeidx += wordidx
            # print(wordsidx)
        wordsidxDiff = []
        count = 0
        findidx = []
        wordsidx.sort()
        print(wordsidx)
        if len(words) == 1:
            return wordsidx
        for i in range(1,len(wordsidx)):
            wordsidxDiff.append(wordsidx[i]-wordsidx[i-1])
            # print(wordsidxDiff)
            if wordsidxDiff[i-1] == wlength:
                if len(words) - 1 ==1:
                     findidx.append(wordsidx[i]-wlength*(len(words)-1))
                elif wordsidxDiff [i-1] == wordsidxDiff[i-2] or i == 1:
                    count += 1
                    if count == len(words)-1: # find all word
                        # print(wordsidx[i]-wlength*len(words))
                        findidx.append(wordsidx[i]-wlength*(len(words)-1))
                else:  # not consecutive anymore
                    count = 1
        return findidx

sol = Solution()
# res = sol.findSubstring("wordgoodstudentgoodwordstudentgoodword",
# ["word","good"])
# print(res)
# res = sol.findSubstring("barfoomanthefoobarman",['bar','foo','man'])
# print(res)
# res = sol.findSubstring("barfoomanhalthefoohalbarman",['bar','hal','foo','man'])
# print(res)
res = sol.findSubstring("affeqqwafdawefe",["a",'f'])
print(res)





