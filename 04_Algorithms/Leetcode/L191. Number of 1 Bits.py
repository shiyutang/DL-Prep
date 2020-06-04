class Solution(object):
    def hammingWeight(self, n):
        cont = 0
        while n:
            if n-int(n&(n-1)) == 1:
                cont += 1
            n = n>>1
        return cont

sol = Solution()
print(sol.hammingWeight(0b1111000101010))
print(sol.hammingWeight(0b11111111111111111111111111111101))