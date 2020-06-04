# class Solution:
# 	def accountsMerge(self, accounts):
# 		if accounts == [] or accounts == [[]]:
# 			return accounts
# 		self.emailDict = {}
# 		self.validIndex = []


# 		def merge(accounts,index1,index2,emailIdx):
# 			emails = accounts[index2][emailIdx:]
# 			for j,email in enumerate(emails):
# 				if not email in accounts[index1]:
# 					accounts[index1].append(email)
# 					# print(email,self.emailDict[email],index1)
# 					if email in self.emailDict and \
# 					   self.emailDict[email] != index1 and \
# 					   self.emailDict[email] in self.validIndex:
# 						# print('I am merging {} and {} because of {}'.format(index1,self.emailDict[email],email))
# 						if self.emailDict[email] != index2:
# 							accounts = merge(accounts,index1,self.emailDict[email],emailIdx+j)
# 						self.emailDict[email] = index1

# 			self.validIndex.remove(index2)
# 			return accounts

# 		for i, account in enumerate(accounts):
# 			self.validIndex.append(i)
# 			print('account,i',account,i)
# 			j = 0
# 			while j < len(account)-1:
# 				email = account[j+1]
# 				if email in self.emailDict: 
# 					if self.emailDict[email]!=i:
# 						print('I am merging {} and {} because of {}'.format(self.emailDict[email],i,email))
# 						accounts = merge(accounts, self.emailDict[email],i,j)
# 						print(accounts,self.validIndex)
# 						break
# 					else:
# 						# print('account[j]',account[j+1])
# 						del account[j+1]
# 						j -= 1
# 				else:
# 					self.emailDict[email] = i
# 				j += 1

# 		# print('self.validIndex',self.validIndex)
# 		for i,idx in enumerate(self.validIndex):
# 			account = accounts[idx]
# 			emailstmp = account[1:]
# 			emailstmp.sort()
# 			accounts[i][0] = account[0]
# 			accounts[i][1:] = emailstmp
# 		# print('self.emailDict',self.emailDict)

# 		return accounts[0:len(self.validIndex)]


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

    def countUp(self):   # return result in group form
        for key in self.father_dict:
            self.find_head(key)
        resDict = {}
        for key in self.father_dict:
            if self.father_dict[key] in resDict:
                resDict[self.father_dict[key]].append(key)
            else:
                resDict[self.father_dict[key]] = [key]
        # print(resDict,self.father_dict)
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



class Solution(object):
	def accountsMerge(self, accounts):
		if accounts == [] or accounts == [[]]:
			return accounts

		accountId = [i for i in range(len(accounts))]
		accounts_UF = UnionFindSet(accountId)
		self.emailDict = {}

		for i, account in enumerate(accounts):
			j = 0
			while j < len(account)-1:
				email = account[j+1]
				if email in self.emailDict: 
					if self.emailDict[email]!=i:
						accounts_UF.union(self.emailDict[email],i)
					else:
						del account[j+1]
						j -= 1
				else:
					self.emailDict[email] = i
				j += 1


		resDict = accounts_UF.countUp()
		result = []
		for key in resDict:
			result.append([accounts[resDict[key][0]][0]])
			for val in resDict[key]:
				emails = accounts[val][1:]
				for email in emails:
					if not email in result[-1]:
						result[-1].append(email)

			result[-1].sort()

		return result





sol = Solution()
print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print(sol.accountsMerge([[]]))
# print(sol.accountsMerge([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
# 	["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
# 	["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]))


# print(sol.accountsMerge([["David","David0@m.co","David1@m.co"],
# 	["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],
# 	["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))# [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]


# print(sol.accountsMerge([["John","John5@m.co","John3@m.co","John1@m.co"],
# 	["David","David3@m.co","David1@m.co","David1@m.co"],
# 	["Lily","Lily2@m.co","Lily5@m.co","Lily0@m.co"],
# 	["Isa","Isa2@m.co","Isa3@m.co","Isa2@m.co"],
# 	["Bob","Bob0@m.co","Bob2@m.co","Bob1@m.co"]]))