# 在 get 部分还是操作太多了，使用哈希表来记录已有操作节省空间, 同时保存了记录，不用反复寻找
from collections import defaultdict


class SnapshotArray:
    def __init__(self, length: int):
        self.data = defaultdict(dict)
        self.sid = -1
        self.length = length

    def set(self, index: int, val: int) -> None:
        self.data[self.sid+1][index] = val
        print(self.data)

    def snap(self) -> int:
        self.sid += 1
        self.data[self.sid] = self.data[self.sid - 1].copy()
        return self.sid

    def get(self, index: int, snap_id: int) -> int:
        res = self.data[snap_id].get(index, 0)

        return res
