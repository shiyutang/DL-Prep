class Solution:
    def preprocessing(self, start, end):
        self.r = end - start + 1
        self.values = [i for i in range(start, end + 1)]
        self.factors = [i for i in range(self.r)]
        primes = self.eratosthenes(10 ** 6 + 5)

        # 统计a,b 范围内的因子个数
        for p in primes:
            s = start - (start % p)  # 从一个可以被质数 p 整除的数开始
            s = [s, s+p][start > s]
            for i in range(s, end+1, p):
                k = 0
                while self.values[i-start] % p == 0:
                    self.values[i-start] /= p
                    k += 1
                self.factors[i-start] *= k+1

        for i in range(self.r):
            if self.values[i] != 1:
                self.factors[i] *= 2
            self.values[i] = start + i

    def solve(self, divisor):
        sum = 0
        for i in range(self.r):
            k = 0
            while self.values[i] % divisor == 0:
                self.values[i] /= divisor
                k += 1
            sum += self.factors[i] / (k+1)
            self.values[i] = a+i
        return int(sum)

    def eratosthenes(self, n):
        is_prime = [True] * (n + 1)  # 建立一个boolean类型的数组，用来存储你要判断某个范围内自然数中的质数
        for i in range(2, int(n ** 0.5) + 1):  # 只需要到根号就可以了，因为根号的平方超出想求的范围，根号之后的已经被之前的倍数更新过了
            if is_prime[i]:  # 如果原本 i 是质数，从小到o'p大，能保证前面的一定是质数
                for j in range(i * i, n + 1, i):  # 则 i 的所有倍数均不是质数
                    is_prime[j] = False
        return [x for x in range(2, n + 1) if is_prime[x]]


t, a, b = list(map(int, input().split(' ')))
sol = Solution()
sol.preprocessing(a,b)

for _ in range(t):
    d = int(input())
    print(sol.solve(d))
