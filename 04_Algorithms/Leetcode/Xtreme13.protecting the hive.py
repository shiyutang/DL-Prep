from collections import defaultdict


class UnionFindSet(object):
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def add_node(self, node):
        self.father_dict[node] = node
        self.size_dict[node] = 1

    def find_head(self, node):
        """使用递归的方式来查找父节点
        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        father = self.father_dict[node]
        if node != father:  # node == father 代表这个节点是代表性节点，是真正得祖先
            father = self.find_head(father)
        self.father_dict[node] = father
        return father

    def countUp(self):
        """
        返回每个 father 节点的孩子
        :return: children dict
        """
        for key in self.father_dict:  # update father
            self.find_head(key)
        chdrDict = {}
        for key in self.father_dict:
            if self.father_dict[key] in chdrDict:
                chdrDict[self.father_dict[key]].add(key)
            else:
                chdrDict[self.father_dict[key]] = set([tuple(key)])
        return chdrDict

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

        return a_head, b_head


def findnei(pos, half=True):
    row, col = pos
    if row % 2:
        nei = [(row - 1, col - 1)]
    else:
        nei = [(row - 1, col + 1)]
    nei.extend([(row - 1, col), (row, col - 1)])
    nei.extend([(nei[0][0] + 2, nei[0][1]), (nei[1][0] + 2, nei[1][1]), (row, col + 1)])

    return nei[:3] if half else nei


def validnei(nei):
    return rows >= nei[0] >= 1 and (cols - 1 >= nei[1] >= 1 or (nei[0] % 2 and nei[1] == cols))


rows, cols = list(map(int, input().split(' ')))
UF = UnionFindSet([])
for i in range(1, rows + 1):
    row = input().split(' ')
    for idx, ele in enumerate(row):
        if ele == '1':
            row, col = i, idx + 1
            UF.add_node((row, col))              # 活跃的节点加入并查集
            for nei in findnei((row, col)):      # 之前加入活跃节点的有是邻居的合并
                if validnei(nei) and nei in UF.father_dict:
                    UF.union((row, col), nei)


# preprocessing perimeter
perimeterDict = {}
chdrDict = UF.countUp()  # 以father 牵头的 childrendict
for father in chdrDict:
    totalcnt = 6*len(chdrDict[father])
    activeNeigh = 0
    for child in chdrDict[father]:
        for nei in findnei(child, half=False):
            if validnei(nei) and nei in chdrDict[father]:
                activeNeigh += 1
    perimeterDict[father] = totalcnt - activeNeigh

# print('UF.father_dict, chdrDict,perimeterDict', UF.father_dict, chdrDict,perimeterDict)


numQ = int(input().strip())
actions = []
for q in range(numQ):
    action = input().split(' ')
    node = (int(action[1]), int(action[2]))
    if action[0] == 'a':
        UF.add_node(node)
        perimeterDict[node] = 6

        # 查看邻居节点
        cnt = defaultdict(int)  # head1: cnt1 节点有多少个邻居活跃
        a_head = UF.find_head(node)
        for nei in findnei(node, half=False):
            if validnei(nei) and nei in UF.father_dict:  # 邻居节点活跃
                b_head = UF.find_head(nei)
                if a_head != b_head:                     # 且不在同一个集合中, 统计在另一个集合中的所有邻居节点
                    cnt[b_head] += 2

        # 所有的不同集合，根据统计的结果消去
        for h in cnt:
            if UF.size_dict[a_head] < UF.size_dict[h]:
                perimeterDict[h] += perimeterDict[a_head] - cnt[h]
                perimeterDict.pop(a_head)
                a_head = h
            else:
                perimeterDict[a_head] += perimeterDict[h] - cnt[h]
                perimeterDict.pop(h)

            UF.union(node, h)  # 当前节点和邻居连结之后

    elif action[0] == 'k':
        if node in UF.father_dict:
            head = UF.find_head(node)
            print(perimeterDict[head])
        else:
            print(0)
