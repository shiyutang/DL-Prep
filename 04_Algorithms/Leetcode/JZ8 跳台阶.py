class Solution:
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        elif number < 3:
            return number
        else:
            a = 1
            b = 2
            for i in range(3, number+1):
                res = a + b
                a, b = b, res
                # print(res,a,b)

            return res


sol = Solution()
print(sol.jumpFloor(4))
