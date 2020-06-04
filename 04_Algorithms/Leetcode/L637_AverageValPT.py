class Solution:
    def averageOfLevels(self, root):
        queue = []
        rootlevel = 0
        res = [[] for _ in range(6000)]
        res[rootlevel].append(root.val)
        if root == None:
            return []
        if root.left == None and root.right == None:
            return res[rootlevel]
        queue.append([root,rootlevel])
        while queue != []:
            root,rootlevel = queue.pop()
            if root.left:
                res[rootlevel+1].append(root.left.val)
                queue.append([root.left,rootlevel+1])
            if root.right:
                res[rootlevel+1].append(root.right.val)
                queue.append([root.right,rootlevel+1])
            # print(res)
        averageVal = []
        for sublist in res:
            if sublist!= []:
                if len(sublist) == 1:
                    averageVal.append(sublist[0])
                else:
                    averageVal.append(sum(sublist)/len(sublist))
        # print(averageVal)
        return averageVal