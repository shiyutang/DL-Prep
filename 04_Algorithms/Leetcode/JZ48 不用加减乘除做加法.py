class Solution:
    def Add(self, num1, num2):
        res = (num1 ^ num2) & 0xffffffff  # 关注一开始输入的负数
        while num2 != 0:
            res = (num1 ^ num2) & 0xffffffff
            cin = ((num1 & num2) << 1) & 0xffffffff  # 保留进位的负数
            num2 = cin
            num1 = res
            # print(num1, num2, cin, res)

        if (res & 0x80000000) >> 31 == 1:  # 和32位的16进制数判断是否是负数
            res = -(((~res) + 1) & 0xffffffff)  # 负数要取反加一获得对应的正数再加上符号，不然是得到负数的表示
        else:
            res = res & 0xffffffff  # 对于正数还要截断结果才对
        return res


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = 13, 5
    # data = -85, 107
    res = sol.Add(data[0], data[1])
    print(res)

    if random_samples:
        import random
        for _ in range(times):
            data = random.randint(-100, 200), random.randint(-100, 200)
            print(data)
            res = sol.Add(data[0], data[1])
            print(res)


test(Solution, True)
