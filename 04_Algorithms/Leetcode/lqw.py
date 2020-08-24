#
# reverse string
# @param str string字符串 the stirng
# @return string字符串
#
class Solution:
    def reverseStringI(self, string):
        if not string:
            return string
        words = []
        pre = 0
        for i, ele in enumerate(string):
            if ele == ' ':
                if (i - 1) >= 0 and string[i - 1] != ' ':
                    words.append(string[pre:i])
                pre = i + 1
        words.append(string[pre:])

        for i, word in enumerate(words):
            tmp = ''
            for ele in word[::-1]:
                tmp += ele
            words[i] = tmp + ' '
        ret = ''.join(words)

        return ret[:-1]

sol = Solution()
print(sol.reverseStringI("i am a student"))