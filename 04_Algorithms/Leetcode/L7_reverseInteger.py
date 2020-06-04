# reverse an integer and return 0 if overflow

class Solution:
    def reverse(self, x):
        if x>0:
            sign = 1
        else:
            sign = -1
        single = []
        while x != 0:
            single.append(x%(10*sign))
            x = int(x/10)
        reversedx = 0
        for i in range(len(single)):
            reversedx += single[-1]*(10**i)
            single.pop()
        if reversedx > 2**31 - 1 or reversedx<-2**31:
            return 0
        else:
            return reversedx

def test():
    sol = Solution()
    res = sol.reverse(-234)
    print(res)

test()