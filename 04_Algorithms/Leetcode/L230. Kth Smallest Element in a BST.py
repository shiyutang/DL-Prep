# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        stack = self.preorder_traversal(root,[])
        return stack[k-1]
        


    def preorder_traversal(self,root,res): 
        if not root:
            return 
        self.preorder_traversal(root.left,res)        
        res.append(root.val)
        self.preorder_traversal(root.right,res)  
        return res


