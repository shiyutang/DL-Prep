import copy


def bisect(data, target):
    """
    :param data: list in ascending order
    :param target:
    :return:
    """
    data.sort()
    low, high = 0, len(data) - 1
    mid = int((high - low) / 2 + low)

    while low < high:
        if data[mid] == target:
            return midw
        elif data[mid] > target:
            high = mid
        else:
            low = mid + 1
        mid = int((high - low) / 2 + low)

    return mid


data = [1, 2, 3, 4, 5, 6, 7, 9]
print(data[bisect(data, 5)])

a = [1, 2, [4, 5], [2, 3, 43]]

c = a[:]
d = copy.deepcopy(a)
d[2][1] = 100
print(d, a)
c[2][1] = 100
print(c, a)

shallow = a
shallow[2] = 1000
print(shallow, a)

a = iter([1, 2, 3])
for i in a:
    print(i)
for i in a:
    print(i)
c = (1, 2, 3)
for i in c:
    print(i)
for i in c:  # 只能使用一次
    print(i)
