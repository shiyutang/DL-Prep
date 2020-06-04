class UnionFindSet(object):
    """并查集"""
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

        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        father = self.father_dict[node]
        if(node != father):  # node == father 代表这个节点是代表性节点，是真正得祖先
            father = self.find_head(father)
        self.father_dict[node] = father
        return father


    def countUp(self):
        for key in self.father_dict:
            self.find_head(key)
        resDict = {}
        for key in self.father_dict:
            if self.father_dict[key] in resDict:
                resDict[self.father_dict[key]].append(key)
            else:
                resDict[self.father_dict[key]] = [key]
        # print('resDict,self.father_dict',resDict,self.father_dict)
        return resDict


    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find_head(node_a) == self.find_head(node_b)


    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find_head(node_a)
        b_head = self.find_head(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size
        # print(self.father_dict)


class Solution:
	def numIslands(self, grid):
		if grid == [[]] or grid == []:
			return 0

		n,m = len(grid),len(grid[0])

		def AdjPos(x):
			# print(pos)
			fun = lambda x: 0<=x[0]<n and 0<=x[1]<m and grid[x[0]][x[1]] == '1'
			res = list(filter(fun,[(x[0] + 1, x[1]), (x[0] - 1, x[1]), (x[0], x[1] + 1), (x[0], x[1] - 1)]))
			# print(res)
			return res

		posList = [(i,j) for i in range(n) for j in range(m)]
		# print('posList',posList)
		connectSet = set()

		UF = UnionFindSet(posList)
		for pos in posList:
			if grid[pos[0]][pos[1]] == '1':
				adjpoint = AdjPos(pos)
				for point in adjpoint:
					if not (point,pos) in connectSet:
						# print('pos,point',pos,point)
						UF.union(pos,point)
						connectSet.add((pos,point))

		resDict = UF.countUp()
		islandCnt = 0
		for key in resDict:
			if grid[key[0]][key[1]] == '1':
				islandCnt += 1

		return islandCnt





sol = Solution()
# print(sol.numIslands([["1","1","1","1","0"],
# 					  ["1","1","0","1","0"],
# 					  ["1","1","0","0","0"],
# 					  ["0","0","0","0","0"]]))

# print(sol.numIslands([["1","0","1","1","0"],
# 					  ["1","0","0","1","1"],
# 					  ["1","0","0","0","0"],
# 					  ["0","1","0","1","0"]]))

print(sol.numIslands([["1","0","1","1","0"],
					  ["1","0","0","1","1"],
					  ["1","0","0","1","0"],
					  ["1","1","0","1","0"],
					  ["1","0","1","1","0"],
					  ["1","0","0","1","1"],
					  ["1","0","0","0","0"],
					  ["0","1","0","1","0"]]))


