import sys

n = sys.stdin.readline().strip()  # 去除首尾空格
line = sys.stdin.readline().strip().split(' ')  # 返回分割好的字符列表
sys.stdout.write(n)
print(line)
