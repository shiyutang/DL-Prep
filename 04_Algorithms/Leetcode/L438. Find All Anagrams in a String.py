class Solution:
    def findAnagrams(self, s: str, p: str):
        a = list(set(s + p))
        a.sort()
        aLen, pLen = len(a), len(p)
        ret = []
        pfreq, sfreq = [0] * aLen, [0] * aLen

        # p state list
        for ele in p:
            idx = a.index(ele)
            pfreq[idx] += 1
        # print(pfreq, a)

        # s state list and cmp
        for i in range(len(s) - pLen + 1):
            slice = s[i:i + pLen]
            if i == 0:
                for ele in slice:
                    idx = a.index(ele)
                    sfreq[idx] += 1
            else:
                idx = a.index(s[i - 1])
                sfreq[idx] -= 1
                idx = a.index(s[i + pLen - 1])
                sfreq[idx] += 1
                print(s[i - 1], s[i + pLen - 1])
            if sfreq == pfreq:
                ret.append(i)
            # print(sfreq, ret)

        return ret


# 使用字符哈希来比较，不用list 存储节省空间，另外加减比pop，push，省时间
class Solution:
    def findAnagrams(self, s: str, p: str):

        hashp = sum(hash(ch) for ch in p)
        hashi = sum(hash(ch) for ch in s[:len(p)])

        idx_anagrams = []

        if hashi == hashp:
            idx_anagrams.append(0)

        for idx, (ch_out, ch_in) in enumerate(zip(s, s[len(p):]), 1):
            hashi += hash(ch_in) - hash(ch_out)
            if hashi == hashp:
                idx_anagrams.append(idx)

        return idx_anagrams

sol = Solution()
s, p = "cbaebabacd", "abc"
s, p = "abab", "b"
s, p = "", "b"
sol.findAnagrams(s, p)
