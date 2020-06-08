# 注意，在对 list 中内容进行操作时，可以直接使用 while 循环，而不要对 list 的长度/内容进行循环,
# 因为计算的结果需要 in_place 地更改用于之后地计算，就会涉及到index的变化
class Solution:
    def calculate(self, s: str) -> int:
        sep = []
        for ele in s.split():
            sep += list(ele)

        def isnum(n):
            if n != '+' and n != '-' and n != '*' and n != '/':
                return True
            else:
                return False

        # merge number
        idx = 0
        while idx < len(sep):
            if idx > 0 and isnum(sep[idx]) and isnum(sep[idx - 1]):
                sep[idx - 1] = ''.join((sep[idx - 1], sep[idx]))
                sep.pop(idx)
            else:
                idx += 1
            print(sep)

        # * and / first
        idx = 0
        while idx < len(sep):
            if sep[idx] == '*':
                res = int(sep[idx - 1]) * int(sep[idx + 1])
            elif sep[idx] == '/':
                res = int(int(sep[idx - 1]) / int(sep[idx + 1]))
            else:
                idx += 1
                continue
            sep[idx - 1] = str(res)
            sep.pop(idx)
            sep.pop(idx)
            print(sep)

        idx = 0
        while idx < len(sep):
            if sep[idx] == '+':
                res = int(int(sep[idx - 1]) + int(sep[idx + 1]))
            elif sep[idx] == '-':
                res = int(int(sep[idx - 1]) - int(sep[idx + 1]))
            else:
                idx += 1
                continue
            sep[idx - 1] = str(res)
            sep.pop(idx)
            sep.pop(idx)
            print(sep)

        return ''.join(sep)


# test
def test(method, random_samples=False):
    sol = method()
    params = " 3+5 / 2 "
    params = " 444"
    params = "1337"
    params = "10-2147483647"
    # params = "1*2-3/4+5*6-7*8+9/10"
    params = " 3 1/15 1 *21+ 21*4 11/51*31 - 2 "
    res = sol.calculate(params)
    print(' and the res is', res)


test(Solution, False)
