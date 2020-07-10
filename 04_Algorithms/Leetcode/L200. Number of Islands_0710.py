class UnionFindSet(object):
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find_head(self, node):
        """使用递归的方式来查找父节点
        """
        father = self.father_dict[node]
        if node != father:  # node == father 代表这个节点是代表性节点，是真正得祖先
            father = self.find_head(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find_head(node_a) == self.find_head(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find_head(node_a)
        b_head = self.find_head(node_b)

        if a_head != b_head:
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if a_set_size >= b_set_size:
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size


class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        def filter_helper(coord):
            x, y = coord
            if len(grid) > x >= 0 and len(grid[0]) > y >= 0 and grid[x][y] == '1':
                return True
            return False

        data = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        unionset = UnionFindSet(data)

        zerocnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    for nei in filter(filter_helper, ((i - 1, j), (i, j - 1))):
                        unionset.union(nei, (i, j))
                else:
                    zerocnt += 1

        fatherset = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                father = unionset.find_head((i, j))
                fatherset.add(father)

        return len(fatherset) - zerocnt


sol = Solution()
print(sol.numIslands([["1", "1", "1", "1", "0"],
                      ["1", "1", "0", "1", "0"],
                      ["1", "1", "0", "0", "0"],
                      ["0", "0", "0", "0", "0"]]))

print(sol.numIslands([["1", "0", "1", "1", "0"],
                      ["1", "0", "0", "1", "1"],
                      ["1", "0", "0", "0", "0"],
                      ["0", "1", "0", "1", "0"]]))

print(sol.numIslands([["1", "0", "1", "1", "0"],
                      ["1", "0", "0", "1", "1"],
                      ["1", "0", "0", "1", "0"],
                      ["1", "1", "0", "1", "0"],
                      ["1", "0", "1", "1", "0"],
                      ["1", "0", "0", "1", "1"],
                      ["1", "0", "0", "0", "0"],
                      ["0", "1", "0", "1", "0"]]))
