# 质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。其可以主要用于哈希表，加密算法等
# 总结：
# 1. 埃筛法： 占用 O(N) 内存， 一次可以计算一个范围内的所有质数，因为每个数都需要更新一遍，因此计算复杂度为 O(N), 但是判断质数也需要 O(N)
# 2. 根号整除判断：计算复杂度为O(n**0.5), 空间复杂度为O(1), 适合判断质数时使用，但是速度依旧较慢
# 3. Miller–Rabin 质数检测：速度较快，但是有可能出错，基于蒙特卡洛随机算法，随着测试的次数增加，伪质数的概率呈 1/(4**n) 递减。如果是合数一定是合数，如果是质数不一定是质数
# 4. AKS 质数检测： 说是多项式时间，但是实际应用依旧很慢

##############
# 埃筛法求质数 #
# 初始化：你要输出小于200的质数，你需要建立一个大小为201（建立201个存储位置是为了让数组位置与其大小相同）的boolean数组，初始化为true。
from time import time


def eratosthenes(n):
    is_prime = [True] * (n + 1)  # 建立一个boolean类型的数组，用来存储你要判断某个范围内自然数中的质数
    for i in range(2, int(n ** 0.5) + 1):  # 只需要到根号就可以了，因为根号的平方超出想求的范围，根号之后的已经被之前的倍数更新过了
        if is_prime[i]:  # 如果原本 i 是质数，从小到o'p大，能保证前面的一定是质数
            for j in range(i * i, n + 1, i):  # 则 i 的所有倍数均不是质数
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]


##############
# 根号整除判断 #
# 如果一个数能被它的最小质因数整除的话，那它肯定是合数，即不是质数。所以判断一个数是否是质数，只需判断它是否能被小于它开跟后后的所有数整除
def is_prime_num(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 返回小于r的素数列表 需要时间大于埃式筛法
def oulashai(r):
    prime = [0 for i in range(r + 1)]
    common = []
    for i in range(2, r + 1):
        if prime[i] == 0:
            common.append(i)
        for j in common:
            if i * j > r:
                break
            prime[i * j] = 1
            if i % j == 0:
                break
    return common

# test
num = 10**12
def test(method):
    t1 = time()
    if "era" in method:
        res = eratosthenes(num)
    elif "isp":
        res = []
        for i in range(2, 120000):
            if is_prime_num(i):
                res.append(i)
    else:
        res = oulashai(120000)
    t2 = time()
    return res, t2 - t1


result1, time1 = test("era")
# result2, time2 = test("oula")
result3, time3 = test("isp")

if not result3 == result1:
    print("result1 is {} \nresult2 is {}".format(result1, result3))
print("era needs {} secs; isp needs {} secs".format(time1, time3))
