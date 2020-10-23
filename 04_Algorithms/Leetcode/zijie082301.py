import math

n, k = map(int, input().split(' '))
remaindict = {}
data = list(map(int, input().split(' ')))

for i in range(n):
    remainnum = k - (data[i] % k)
    if remainnum not in remaindict:
        remaindict[remainnum] = [data[i]]
    else:
        remaindict[remainnum].append(data[i])
print(remaindict)


def comb_1(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


cnt = 1 + n
allflag = False
print(cnt)
combs = set()

# 从余0中取一个，余k//2中取一个，余剩下的需要排除掉其他
for key in remaindict:
    tmp = data[:]
    if key == k or key == k / 2:
        reslen = n - len(remaindict[key]) + 1
        # data =
    else:
        if (k - key) not in remaindict:
            if allflag:
                continue
            else:
                reslen = n
                allflag = True
        else:
            reslen = n - len(remaindict[k - key])
    print('reslen',key,reslen)
    for i in range(2,reslen):
        cnt += comb_1(n, i)
        cnt = cnt % 1000000007
        print(cnt)

if not allflag:
    cnt += 1

print(cnt % 1000000007)

# 4 3
# 1 2 3 4
