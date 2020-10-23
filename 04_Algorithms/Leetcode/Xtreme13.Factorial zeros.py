class Solution:
    def solve(self, b, z):
        culmul = 1
        target = '0' * z
        for i in range(2, 7*10**2):
            culmul *= i
            res = self.str_base(culmul, b)
            # print(res)
            if res[:z] == target and res[z] != '0':
                return i
        return -1

    def digit_to_char(self, digit):
        if digit < 10:
            return str(digit)
        return chr(ord('a') + digit - 10)

    def str_base(self, number, base):
        res = ['-', ''][number >= 0]
        d, m = divmod(number, base)
        res += self.digit_to_char(m)
        while d > 0:
            d, m = divmod(d, base)
            res = res + self.digit_to_char(m)
        return res


T = int(input())
sol = Solution()
for _ in range(T):
    base, zeros = list(map(int, input().strip().split(' ')))
    print(sol.solve(base, zeros))
