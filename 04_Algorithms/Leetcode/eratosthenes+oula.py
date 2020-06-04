def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]


#返回小于r的素数列表
def oulashai(r):
	prime = [0 for i in range(r+1)]
	common = []
	for i in range(2,r+1):
		if prime[i] == 0:
			common.append(i)
		for j in common:
			if i*j>r:
				break
			prime[i*j] = 1
			if i%j == 0:
				break
	return common

print('oula',oulashai(1154))

print('era',eratosthenes(1154))
