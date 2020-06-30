# -*- coding:utf-8 -*-
# 字符串转换：按照其中的字符依次转换
# 可能的字符：'0'-'9', ‘+-’, ‘eE’, ‘.’
# 合法示例：‘12.57’，‘+1e10’，‘10.4e-5’，‘3e+6’，‘.6’
# 非法示例：‘1s8’，‘1-5’，‘10e0.4’，‘6.7.8’，‘+1+5’
# 正负号只能出现在首位和e之后；'.'只能出现在e之前且只能出现一次,e/E 只能出现在数字之后，且只能出现一次

class Solution:
    def StrToInt(self, s: str):
        if not s:
            return 0
        eMark, dotMark, negMark = False, False, False
        beforeE, afterE = '', ''

        def num2int(string):
            res = 0
            dot = False
            for index in range(len(string)):
                if string[index] == '.':
                    dot = True
                    break
            if dot:
                for cnt, idx in enumerate(range(index - 1, -1, -1)):
                    res += int(string[idx]) * (10 ** cnt)
                for cnt, idx in enumerate(range(index + 1, len(string))):
                    # print(string,string[idx])
                    res += int(string[idx]) / (10 ** (cnt+1))
            else:
                for cnt, idx in enumerate(range(len(string) - 1, -1, -1)):
                    res += int(string[idx]) * (10 ** cnt)
            return res

        # 判断是否合法并记录前后字符串
        for i, ele in enumerate(s):
            if ele == '+' or ele == '-':
                if i != 0 and (s[i - 1] != 'e' and s[i - 1] != 'E'):
                    return 0
                else:
                    if ele == '-' and (s[i - 1] != 'e' and s[i - 1] != 'E'):
                        negMark = True
            elif ele == 'e' or ele == 'E':
                if i == 0 or eMark or not s[i - 1].isdigit():
                    return 0
                else:
                    eMark = True
            elif ele == '.':
                if dotMark or eMark:
                    return 0
                else:
                    dotMark = True
                    if not eMark:
                        beforeE += ele
                    else:
                        afterE += ele
            elif ele.isdigit():
                if not eMark:
                    beforeE += ele
                else:
                    afterE += ele
            else:
                return 0

        beforeEnum = num2int(beforeE)
        afterEnum = num2int(afterE)
        ret = beforeEnum*(10**afterEnum)
        return [ret, -ret][negMark]

sol = Solution()
print(sol.StrToInt(''))
print(sol.StrToInt('1s8'))
print(sol.StrToInt('1-5'))
print(sol.StrToInt('10e0.4'))
print(sol.StrToInt('6.7.8'))
print(sol.StrToInt('+1+5'))
print(sol.StrToInt('12.57'))
print(sol.StrToInt('.6'))
print(sol.StrToInt('1e10'))
print(sol.StrToInt('3e+6'))
print(sol.StrToInt('10.4e-5'))
