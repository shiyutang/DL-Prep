class UnionFindSet(object):
    def __init__(self, data_list):
        """
        :param data_list: 初始化的数据集
        """
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find_head(self, node):
        father = self.father_dict[node]
        if node != father:  # node == father 代表这个节点是代表性节点，是真正得祖先
            father = self.find_head(father)
        self.father_dict[node] = father
        return father

    def countUp(self):
        for key in self.father_dict:
            self.find_head(key)

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
        # print(self.father_dict)


class Solution2:
    def longestConsecutive(self, nums):
        UF = UnionFindSet(nums)
        for num in nums:
            if num - 1 in nums and num + 1 in nums:
                UF.union(num - 1, num + 1)
            elif num - 1 in nums:
                UF.union(num, num - 1)
            elif num + 1 in nums:
                UF.union(num + 1, num)

        UF.countUp()
        # print(UF.father_dict)
        maxval = 0
        for key in UF.size_dict:
            if UF.size_dict[key] > maxval:
                maxval = UF.size_dict[key]

        return maxval


class Solution1:
    def longestConsecutive(self, nums):
        nums = set(nums)
        print(nums)
        best = 0
        for i in nums:
            if (i - 1) not in nums:  # 保证从头开始
                y = i + 1
                while y in nums:  # 用集合使得查找操作为O（1）
                    y += 1
                best = max(best, y - i)
        return best


# 使用哈希表加速查找效率，其中我们只需要找到第一个开始的位置计算连续子序列就可以
class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = set(nums)
        ret = 0
        for num in nums:
            if num - 1 not in nums:
                tmp = num + 1
                cnt = 1
                while tmp in nums:
                    tmp += 1
                    cnt += 1

                ret = max(ret, cnt)

        return ret


sol = Solution()
a = [100, 4, 200, 1, 3, 2, 102, 300, 7, 10, 8, 9, 5, 6]
print(sol.longestConsecutive([0, 0, -1]))
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([]))
print(sol.longestConsecutive(a))

print(sol.longestConsecutive([-8, -4, 9, 9, 4, 6, 1, -4, -1, 6, 8]))
