def solve(start, end):
    start.sort()
    end.sort()
    cnt = 0
    maxval = 0
    s, e = 0, 0
    while s < len(start):
        if start[s] < end[e]:
            cnt += 1
            maxval = max(maxval, cnt)
            s += 1
        else:
            cnt -= 1
            e += 1
    print(maxval)


while 1:
    try:
        n = int(input())  # 去除首尾空格
        start, end = [], []
        for i in range(int(n)):
            line = input().split()  # 返回分割好的字符列表
            start.append(int(line[0]))
            end.append(int(line[1]))

        solve(start, end)
    except:
        break
