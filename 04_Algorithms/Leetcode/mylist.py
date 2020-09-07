class MyList(object):
    def __init__(self, data):
        self.data = data
        self.idx = -1

    def __new__(cls, *args, **kwargs):
        pass

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.idx += 1
        if self.idx >= len(self.data):  # 退出循环的条件
            raise StopIteration()
        return self.data[self.idx]

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.data[item]
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            print(item)

            L = []
            for i in range(start, stop, step):
                L.append(self.data[i])

            return L


c: MyList = MyList((1, 2, 3, 4, 2, 1, 3, 2, 3, 1, 3, 5, 6, 7, 4, 2))
print(c[1], c[1:10], c[1:12:2], c[1:13:-1], c[:10:2])
for ele in c:
    print(ele)
