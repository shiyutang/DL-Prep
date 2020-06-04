class Solution(object):
    def diffWaysToCompute(self, input):
        res = []
        if input.isdigit():
            return [int(input)]
        for i in range(len(input)):
            if input[i] in '+-*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for m in res1:
                    for n in res2:
                        if input[i] == '+':
                            res.append(m+n)
                        elif input[i] == '-':
                            res.append(m-n)
                        else:
                            res.append(m*n)
        return res

sol = Solution()
res = sol.diffWaysToCompute("2-1-1")
print(res)
res = sol.diffWaysToCompute("2*3-4*5")
print(res)