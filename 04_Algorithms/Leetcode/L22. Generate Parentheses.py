# too slow and didn't find all
class Solution:
    def generateParenthesis(self, n: int):
        output = []
        self.memoi = {(1, 1): [[1]], (1, 2): [[0, 1], [1, 0]], (2, 2): [[1, 1], [0, 2]]}

        def subprocess(nump, length, start):
            if (nump, length) in self.memoi:
                return self.memoi[(nump, length)]
            elif nump == 1:
                res = []
                for i in range(length):
                    tmp = [0] * length
                    tmp[i] = 1
                    res.append(tmp)
                self.memoi[(1, length)] = res
                return res
            else:
                if n == length:
                    result = [[0] * length]
                    result[0][-1] = length
                else:
                    result = []
                for i in range(1, length):
                    result += subprocess(i, length - 1, start=i - 1)
                self.memoi[(nump, length)] = result

                return result

        # format output
        res = subprocess(n, n, start=0)
        for item in res:
            tmp = [0] * n
            tmp[:len(item)] = item
            k = n - sum(item)
            string = ''
            for ele in tmp:
                string += '('
                string += ')' * ele
            string += ')' * k
            output.append(string)

        return output

# 其他人的回溯
class Solution:
    def generateParenthesis(self, n: int):  # 只要左边大于右边，就可以继续向下接
        ret = []

        def helper(left, right, temp):
            if left == 0 and right == 0:
                ret.append(temp)
                return
            if left > 0:
                helper(left - 1, right, temp + "(")
            if right > left and right > 0:
                helper(left, right - 1, temp + ")")

        helper(n, n, "")
        return ret


# 回溯法：只要当前合理就向下走，如果不合理就不走，走到最下面就满足条件回升，不然就不满足条件依旧回升
class Solution1:
    def generateParenthesis(self, n: int):  # 只要左边大于右边，就可以继续向下接
        res = []

        def subprocess(left, right, string):
            if left == right and left == 0:
                res.append(string)
            if 0 < left <= right:
                subprocess(left - 1, right, string + '(')
            if right > 0:
                subprocess(left, right - 1, string + ')')

        subprocess(n, n, '')
        return res


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    n = 4
    res = sol.generateParenthesis(n)
    print('the result is', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            print('n', len1)
            res = sol.generateParenthesis(len1)
            print('the result is', res)


test(Solution, False)
test(Solution1, False)

