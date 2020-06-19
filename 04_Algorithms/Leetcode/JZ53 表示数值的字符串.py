class Solution:
    # s字符串
    def isNumeric(self, s):
        hasE = False
        hasdecimal = False
        for i in range(len(s)):
            if s[i] == '.':
                if i != 0:
                    if hasE or hasdecimal or i + 1 >= len(s) or not (s[i - 1].isdigit() or s[i-1] == '-' or s[i-1] == '+') or not s[i + 1].isdigit():
                        return False
                hasdecimal = True
            elif s[i] == 'e' or s[i] == 'E':
                if i - 1 < 0 or i + 1 >= len(s) or not s[i - 1].isdigit() or (
                        not s[i + 1].isdigit() and s[i + 1] != '-' and s[i + 1] != '+'):
                    return False
                hasE = True
            elif s[i] == '-' or s[i] == '+':
                if not (i == 0 or (
                        i - 1 > 0 and i < len(s) and (s[i - 1] == 'E' or s[i - 1] == 'e') and (s[i + 1].isdigit() or s[i+1] == '.'))):
                    return False
            elif s[i].isdigit():
                continue
            else:
                return False
        return True

sol = Solution()
print(sol.isNumeric('12e'))
print(sol.isNumeric("123.45e+6"))
print(sol.isNumeric("-.2e+6"))

