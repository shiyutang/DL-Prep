# 按照镜面对称的方法构造格雷码，镜面对称只变换最前面一位，其他按照镜面对称，保证交替只变换一位

class Solution:
    def grayCode(self, n: int):
        if n == 0:
            return [0]
        ret = ['0', '1']
        for i in range(2, n + 1):
            pp = len(ret)
            for j in range(pp - 1, -1, -1):
                ret.append('1' + ret[j])
            for j in range(pp):
                ret[j] = '0' + ret[j]
        print(ret)

        for i, ele in enumerate(ret):
            ret[i] = int(ele, base=2)

        return ret


sol = Solution()
print(sol.grayCode(3))
print(sol.grayCode(0))
print(sol.grayCode(1))
print(sol.grayCode(2))
