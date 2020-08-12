class Solution:
    def evalRPN(self, tokens) -> int:
        operator = ['+', '-', '*', '/']
        data = []
        for token in tokens:
            if token in operator:
                # print(data)
                x2, x1 = data.pop(-1), data.pop(-1)
                res = int(eval(x1 + token + x2))
                # print(res)
                data.append(str(res))
            else:
                data.append(token)
        return int(data[0])


sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))
print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(sol.evalRPN([]))
