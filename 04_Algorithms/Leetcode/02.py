import sys


class task:
    def eliminate(self, slist):

        for ele in slist:
            cnt = 0
            while ele != 0:
                ele = ele // 2
                cnt += 1
            print(cnt)


cases = sys.stdin.readline().strip()  # 去除首尾空格
ret = []
for i in range(int(cases)):
    t = sys.stdin.readline().strip()  # 返回分割好的字符列表
    ret.append(int(t))
sol = task()
sol.eliminate(ret)
