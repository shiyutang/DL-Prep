import itertools

n, k = map(int, input().split(' '))
remaindict = {}
data = list(map(int, input().split(' ')))

cnt = 1
if len(data) > 1:
    cnt += n
# print(cnt)
for i in range(2, len(data)):
    res = itertools.combinations(data, i)
    for combs in res:
        eleset = set()
        flag = False
        for ele in combs:
            if not ele%k in eleset:
                eleset.add(k - ele % k)
            else:
                flag = True
                break
        if not flag:
            cnt += 1
        # print(combs,cnt)
print(cnt)

