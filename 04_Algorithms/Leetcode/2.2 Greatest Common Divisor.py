# 最大公因数：能同时被俩个数整除的数的最大值
# INPUT a, b to find the b is always the smaller one
def gcd(a, b):  # O(log(a+b))
    while b:
        r = a % b
        a = b
        b = r
    return a


# 拓展的欧几里得可以求得 a,b 的最大公因数和对应的组合系数
# 即 q = gcd(a,b) = ax+by 中 q, a, b
# 根据我们已知 x*a = 1 (mod n) 要求a， 那么 gcd(x, n) = 1 = a*x + b*n
# 则拓展欧几里得中 x 之前的系数就是 x 的模逆元

def ext_euclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_euclid(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


# test

import random

num_samples = 100
alist = [random.randint(1, 1e2) for i in range(num_samples)]
blist = [random.randint(1, 1e2) for i in range(num_samples)]


def test(aL, bL, method):
    res = []
    for a, b in zip(aL, bL):
        if "ext" in method:
            res.append(ext_euclid(a, b))
        else:
            res.append(gcd(a, b))
    return res


res1 = test(alist, blist, 'ext')
res2 = test(alist, blist, 'gcd')
print(res1)
print(res2)

for i, (a, b) in enumerate(zip(alist, blist)):
    print('a is {}, b is {}, and their gcd is {} and {} and is combined through {}a + {}b'.format(a, b, res1[i][2],
                                                                                                  res2[i], res1[i][0],
                                                                                                  res1[i][1]))
