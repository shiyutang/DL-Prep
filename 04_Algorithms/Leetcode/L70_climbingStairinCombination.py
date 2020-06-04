from scipy.special import comb, perm
#class Solution:
def climbStairs(number):
    totalNumber = number//2
    sum = 0
    for i in range(totalNumber+1):
        sum += comb(number-i,i)
    return int(sum)

def test():
    res = climbStairs(100)
    print(res)

test()