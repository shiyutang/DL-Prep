
## UF with edge weight 
# class UnionFindSet1(object):
#     """并查集"""
#     def __init__(self, data_list):
#         """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
#         初始化的时候，将节点的父节点设为自身，size设为1"""
#         self.father_dict = {}

#         for node in data_list:
#             self.father_dict[node] = [node,1]
            

#     def find_head(self, node):
#         father = self.father_dict[node][0]
#         val = self.father_dict[node][1]

#         if(node != father):  # node == father 代表这个节点是代表性节点，是真正得祖先
#             self.father_dict[node][1] *= self.father_dict[father][1]
#             father,fatherVal = self.find_head(father)
#         self.father_dict[node][0] = father

#         return father,self.father_dict[node][1]


#     def countUp(self):
#         for key in self.father_dict:
#             self.find_head(key)

#         return self.father_dict


#     def union(self, node_a, node_b,valAB):
#         """将两个集合合并在一起"""
#         if node_a is None or node_b is None:
#             return

#         a_head,valA_head = self.find_head(node_a)
#         b_head,valB_head = self.find_head(node_b)

#         if(a_head != b_head):
#             val = valA_head/(valB_head*valAB)
#             self.father_dict[b_head] = [a_head,val]
#             # print('self.father_dict',self.father_dict)

# normal UF
class UnionFindSet2(object):
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
        print(resDict,self.father_dict)
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
        print(self.father_dict)




# class UnionFindSet2(object):
#     """并查集"""
#     def __init__(self, data_list):
#         """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
#         初始化的时候，将节点的父节点设为自身，size设为1"""
#         self.father_dict = {}
#         self.size_dict = {}

#         for node in data_list:
#             self.father_dict[node] = node
#             self.size_dict[node] = 1


#     def find_head(self, node):
#         """使用递归的方式来查找父节点

#         在查找父节点的时候，顺便把当前节点移动到父节点上面
#         这个操作算是一个优化
#         """
#         father = self.father_dict[node]
#         if(node != father):  # node == father 代表这个节点是代表性节点，是真正得祖先
#             father = self.find_head(father)
#         self.father_dict[node] = father
#         return father


#     def countUp(self):
#         for key in self.father_dict:
#             self.find_head(key)
#         resDict = {}
#         for key in self.father_dict:
#             if self.father_dict[key] in resDict:
#                 resDict[self.father_dict[key]].append(key)
#             else:
#                 resDict[self.father_dict[key]] = [key]
#         # print(resDict,self.father_dict)
#         return resDict


#     def is_same_set(self, node_a, node_b):
#         """查看两个节点是不是在一个集合里面"""
#         return self.find_head(node_a) == self.find_head(node_b)


#     def union(self, node_a, node_b):
#         """将两个集合合并在一起"""
#         if node_a is None or node_b is None:
#             return

#         a_head = self.find_head(node_a)
#         b_head = self.find_head(node_b)

#         if(a_head != b_head):
#             a_set_size = self.size_dict[a_head]
#             b_set_size = self.size_dict[b_head]
#             if(a_set_size >= b_set_size):
#                 self.father_dict[b_head] = a_head
#                 self.size_dict[a_head] = a_set_size + b_set_size
#             else:
#                 self.father_dict[a_head] = b_head
#                 self.size_dict[b_head] = a_set_size + b_set_size
#         print(self.father_dict)



if __name__ == '__main__':
    # a = ['a','b','c']
    # union_find_set = UnionFindSet1(a)
    # union_find_set.union('a','b',2.0)
    # union_find_set.union('b','c',3.0)
    # print(union_find_set.countUp())

    # a = [100,4,200,1,3,2]
    # union_find_set = UnionFindSet2(a)
    # union_find_set.union(1,3)
    # union_find_set.union(2,4)
    # union_find_set.union(2,3)
    # print(union_find_set.size_dict)
    # # print(union_find_set.is_same_set(2,5))  # True
    # # print('2',union_find_set.father_dict)
    # union_find_set.countUp()

    a = [(1,2),(2,2),(4,1),(3,4),(3,5),(4,3),(5,4),(5,5)]
    union_find_set = UnionFindSet2(a)
    union_find_set.union((1,2),(2,2))
    union_find_set.union((2,2),(1,2))
    union_find_set.union((3,4),(3,5))
    union_find_set.union((3,5),(3,4))
    union_find_set.union((3,4),(4,3))
    union_find_set.union((4,3),(3,4))
    union_find_set.union((4,3),(5,4))
    union_find_set.union((5,4),(4,3))
    union_find_set.union((5,4),(5,5))
    union_find_set.union((5,5),(5,4))
    union_find_set.countUp()
    
