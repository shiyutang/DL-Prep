import sys

def buildGraph(num):
    print(sum(num))





people = sys.stdin.readline().strip()  # 去除首尾空格
ret = []
for i in range(people):
    line = sys.stdin.readline().strip().split(' ')  # 返回分割好的字符列表
    ret.append(line[0])
buildGraph(ret)


