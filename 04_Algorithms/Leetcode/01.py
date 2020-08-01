import sys


class task:
    def solve(self, start, end):
        start.sort()
        end.sort()
        cnt = 0
        maxval = 0
        while start:
            p = start.pop(0)
            cnt += 1
            while end and p >= end[0]:
                end.pop(0)
                cnt -= 1
            maxval = max(maxval, cnt)
            # print(cnt, start, end, maxval)
        return maxval


n = sys.stdin.readline().strip()  # 去除首尾空格
start, end = [], []
for i in range(int(n)):
    line = sys.stdin.readline().strip().split(' ')  # 返回分割好的字符列表
    start.append(line[0])
    end.append(line[1])

# start, end = [1, 1, 2, 3], [2, 3, 4, 4]
# start, end = [0, 1, 5, 0], [1, 4, 6, 49]
# start, end = [1], [3]
sol = task()
res = sol.solve(start, end)

print(res)
